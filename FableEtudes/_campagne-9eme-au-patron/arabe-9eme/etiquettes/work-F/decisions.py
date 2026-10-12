# Décisions de la relecture de fusion (2026-10-12). Lu par fusion.py.
RENAME={}   # ancien id -> id retenu (fusion / renommage) ; les options suivent
DROP={}     # id -> raison (retiré : ses options deviennent muettes)
LABO={}     # id retenu -> (ar,fr,en) libellé réécrit
MUTE={}     # (ch,'f#q',opt) -> raison (option rendue muette)
RETAG={}    # (ch,'f#q',opt) -> (nouvel id, raison)
LOG=[]      # lignes du rapport
RENAME['arabe.shart.ra2isi-bi-tartib-al-dhikr']='arabe.jumla.ra2isi-bi-tartib-al-dhikr'
LABO['arabe.jumla.ra2isi-bi-tartib-al-dhikr']=(
 "تعدُّ الحدثَ المذكورَ أوّلًا أو الّذي تليه الأداةُ حدثًا رئيسيًّا: الرّئيسيُّ حدثُ الجملةِ الّتي لا تبدأُ بالأداةِ (حرفِ الشّرطِ، أداةِ الزّمنِ) أينما وقعتْ",
 "Tu prends pour principal le fait cité en premier ou celui que mène l'outil : le principal est celui de la phrase sans outil (حرف الشرط, أداة الزمن), où qu'elle soit",
 "You take as main the event mentioned first or the one the tool introduces: the main event is in the clause without the tool (condition or time tool), wherever it is")
LOG.append("`arabe.shart.ra2isi-bi-tartib-al-dhikr` (A, ch17, 2 Q) → **`arabe.jumla.ra2isi-bi-tartib-al-dhikr`** : même erreur que le piège 3 de ch03 (« عدُّ الحدثِ الذي تليه الأداةُ حدثًا رئيسيًّا ») ; domaine élargi (حرف الشرط + أداة الزمن), libellé réécrit, 5 Q (17 + 03).")
NEWD={}  # ids neufs créés à la fusion (scission) : id -> (ar,fr,en)
def ren(old,new,why): RENAME[old]=new; LOG.append(f"`{old}` → **`{new}`** : {why}")
def rt(ch,specs,i,why):
    for s in specs.split():
        q,os_=s.split(':')
        for o in os_: RETAG[(ch,q,o)]=(i,why)
def mu(ch,specs,why):
    for s in specs.split():
        q,os_=s.split(':')
        for o in os_: MUTE[(ch,q,o)]=why
# ---------- 1. استدراك : un seul id (A + B) ----------
ren('arabe.rabt.istidrak-bi-ma-yuwafiq','arabe.rabt.istidrak-khalt',"doublon de sens avec `arabe.hijaj.istidrak-khalt` (B) : même règle (le استدراك apporte le contraire de l'attendu), A en production, B en lecture.")
ren('arabe.hijaj.istidrak-khalt','arabe.rabt.istidrak-khalt',"fusionné avec `arabe.rabt.istidrak-bi-ma-yuwafiq` (A).")
LABO['arabe.rabt.istidrak-khalt']=(
 "تخطئُ في الاستدراكِ: يأتي بعدَ «لكنّ، غيرَ أنّ، بيدَ أنّ» بخلافِ ما توهمُ به الجملةُ الأولى؛ فليسَ تقابلًا (بينما) ولا نتيجةً متوقَّعةً (فـ) ولا توكيدًا (إنّ)",
 "Tu vois un استدراك là où il n'y en a pas, ou tu le manques : il dit le contraire de ce que la 1re phrase laissait attendre (لكنّ، غيرَ أنّ) ; ni contraste ni suite attendue",
 "You see an استدراك where there is none, or miss it: it says the opposite of what the first clause led us to expect (لكنّ، غيرَ أنّ); not a contrast, not an expected result")
# ---------- 2. sens des connecteurs : un seul id (A natija + B mu2ashshir) ----------
ren('arabe.rabt.natija-bi-ghayr-al-fa','arabe.rabt.mu2ashshir-ghayr-munasib',"cas particulier (conséquence dite par ثمّ / و / أي) du même geste que `arabe.hijaj.mu2ashshir-ghayr-munasib` (B) : prêter à un connecteur une relation qu'il ne dit pas.")
ren('arabe.hijaj.mu2ashshir-ghayr-munasib','arabe.rabt.mu2ashshir-ghayr-munasib',"fusionné avec `arabe.rabt.natija-bi-ghayr-al-fa` (A) ; domaine `rabt` (أدوات الرّبط) ; les options où le استدراك est en jeu (clé ou option) passent à `arabe.rabt.istidrak-khalt` (14 options).")
LABO['arabe.rabt.mu2ashshir-ghayr-munasib']=(
 "تخلطُ بين معاني المؤشّراتِ: التّعليلُ (لأنّ، إذ)، والنّتيجةُ (فـ، إذن، بناءً على ذلك)، والمهلةُ (ثمّ)، والتّفسيرُ (أي)، والتّقابلُ (بينما)، والإضافةُ (علاوةً على ذلك)",
 "Tu confonds les sens des connecteurs : cause لأنّ، إذ ; conséquence ف، إذن، بناءً على ذلك ; délai ثمّ ; explication أي ; contraste بينما ; ajout علاوةً على ذلك",
 "You mix up what connectors mean: cause لأنّ، إذ; consequence ف، إذن، بناءً على ذلك; delay ثمّ; explanation أي; contrast بينما; addition علاوةً على ذلك")
rt('09','05#2:d 05#3:a quiz#5:ac','arabe.rabt.istidrak-khalt','le استدراك est la clé ou l\'option')
rt('10','04#1:d quiz#6:acd','arabe.rabt.istidrak-khalt','le استدراك est la clé ou l\'option')
rt('11','02#2:bcd quiz#6:bcd','arabe.rabt.istidrak-khalt','le استدراك est la clé ou l\'option')
# ---------- 3. mazid : sens du schème ----------
ren('arabe.mazid.wazn-ma3na-wahid','arabe.mazid.ma3na-bila-nazar-fil-jidhr',"même erreur que l'id large de B (choisir un sens du schème sans examiner racine et phrase) vue de l'autre côté (« un schème = un sens ») ; le libellé fusionné dit les deux.")
LABO['arabe.mazid.ma3na-bila-nazar-fil-jidhr']=(
 "تعطي الوزنَ معنًى دونَ نظرٍ في الجذرِ ولا في الجملةِ: للوزنِ معانٍ عدّةٌ، يحسمُها الجذرُ (فعلٌ، اسمُ شيءٍ، مكانٌ، لونٌ، صفةٌ) والسّياقُ",
 "Tu donnes au schème un sens sans examiner la racine ni la phrase : chaque schème a plusieurs sens ; la racine (verbe, chose, lieu, couleur, qualité) et le contexte tranchent",
 "You give the pattern a meaning without checking the root or the sentence: each pattern has several meanings; the root (verb, thing, place, colour, quality) and context decide")
rt('05','05#5:d','arabe.mazid.wazn-qarib-khalt',"« مُفْتَعَل » pour le patient d'اسْتَخْرَجَ : c'est le schème voisin du tableau (افْتَعَلَ pour اسْتَفْعَلَ), exactement le libellé de `wazn-qarib-khalt` ; `arabe.ishtiqaq.min-fi3l-akhar` (6ᵉ : dériver d'un autre verbe) ne le disait pas")
# ---------- 4. hijaj : thèse réfutée / défendue ; découpage ----------
ren('arabe.hijaj.awwal-ra2y-muthbat','arabe.hijaj.mahdhuda-muthbata-khalt',"cas particulier (l'ordre de mention) de la confusion المدحوضة / المثبتة ; le libellé fusionné le nomme.")
LABO['arabe.hijaj.mahdhuda-muthbata-khalt']=(
 "تخلطُ بين الأطروحةِ المدحوضةِ (رأيِ الخصمِ، وكثيرًا ما تُذكرُ أوّلًا) والمثبتةِ (رأيِ الكاتبِ): التّرتيبُ لا يحسمُ؛ ابحثْ عن «بل»، «والحقُّ أنّ»، «ليس»",
 "Tu confonds thèse réfutée (avis de l'adversaire, souvent cité en premier) et thèse défendue (avis de l'auteur) : l'ordre ne décide pas ; cherche بل، والحقُّ أنّ، ليس",
 "You mix up the refuted thesis (the opponent's view, often stated first) and the defended one (the author's): order decides nothing; look for بل، والحقُّ أنّ، ليس")
ren('arabe.hijaj.jumla-ula-hiya-al-utruha','arabe.hijaj.taqsim-al-binya-khalt',"1 question : c'est un mauvais découpage (la thèse défendue rangée dans la démarche), déjà dit par `taqsim-al-binya-khalt`.")
ren('arabe.hijaj.istintaj-dakhil-al-sayrura','arabe.hijaj.taqsim-al-binya-khalt',"2 questions : mauvais découpage (conclusion rangée dans la démarche) ; le libellé fusionné le nomme.")
LABO['arabe.hijaj.taqsim-al-binya-khalt']=(
 "تقسّمُ النّصَّ تقسيمًا خاطئًا: الأطروحةُ رأيٌ (المدحوضةُ والمثبتةُ معًا إن وُجدتا)، وسيرورةُ الحجاجِ حججٌ وأمثلةٌ، والاستنتاجُ ركنٌ مستقلٌّ يختمُ",
 "Tu découpes mal le texte : la thèse est un avis (réfutée + défendue ensemble s'il y en a deux) ; la démarche = arguments et exemples ; la conclusion est un pilier à part",
 "You split the text wrongly: the thesis is a view (refuted + defended together if both), the argument path = arguments and examples, the conclusion is a pillar of its own")
rt('09','06#1:a','arabe.hijaj.taqsim-al-binya-khalt','question de découpage (أطروحة / سيرورة / استنتاج), pas de nature d\'un élément')
rt('10','01#1:ab 01#2:b','arabe.hijaj.taqsim-al-binya-khalt','question de découpage (أطروحة / سيرورة / استنتاج), pas de nature d\'un élément')
rt('09','06#2:b quiz#4:b','arabe.hijaj.naw3-al-hujja-khalt',"argument d'autorité pris pour « واقعيّة » : ce n'est pas la confusion تاريخيّة / واقعيّة")
rt('10','quiz#5:b','arabe.hijaj.naw3-al-hujja-khalt',"argument d'autorité pris pour « واقعيّة » : ce n'est pas la confusion تاريخيّة / واقعيّة")
# ---------- 5. ch12 : mamdud, maqsur, racine ----------
for o in ['arabe.mamdud.qalb-kull-hamza-waw','arabe.mamdud.hamza-ta2nith-tubqa','arabe.mamdud.hamza-ila-ya-bila-asl']:
    ren(o,'arabe.mamdud.nawa3-al-hamza-khalt',"cas particulier (une des trois hamza traitée comme une autre) de `nawa3-al-hamza-khalt`, dont le libellé dit déjà la règle de chacune.")
ren('arabe.maqsur.muthanna-thulathi-ya-daiman','arabe.maqsur.radd-alif-bila-3add',"erreur symétrique de `muthanna-waw-ghayr-al-asl` (même règle : compter les lettres avant de rendre l'alif) ; 1 question.")
ren('arabe.maqsur.muthanna-waw-ghayr-al-asl','arabe.maqsur.radd-alif-bila-3add',"fusionné avec `muthanna-thulathi-ya-daiman` ; libellé symétrique.")
NEWD['arabe.maqsur.radd-alif-bila-3add']=(
 "تردُّ ألفَ المقصورِ في التّثنيةِ والجمعِ دونَ عدٍّ: فوقَ ثلاثةِ أحرفٍ ياءٌ دائمًا (مُستشفيان، ذِكرَيات)، وفي الثّلاثيِّ إلى أصلِها (عَصَوان، هُديان)",
 "Tu rends l'alif du maqsur au duel ou au pluriel sans compter : au-delà de 3 lettres → toujours ي (مُستشفيان، ذِكرَيات) ; à 3 lettres → son origine (عَصَوان، هُديان)",
 "You turn the maqsur's alif back without counting: beyond 3 letters → always ي (مُستشفيان، ذِكرَيات); with 3 letters → its origin (عَصَوان، هُديان)")
ren('arabe.jidhr.ya-min-al-fi3l-al-mazid','arabe.jidhr.alif-ka-harf-asli',"même erreur (lettre visible prise pour la lettre de racine au lieu de remonter au trilitère) que `alif-ka-harf-asli` ; même piège 12 n°6.")
LABO['arabe.jidhr.alif-ka-harf-asli']=(
 "تعدُّ الألفَ أو الياءَ الظّاهرةَ من حروفِ الجذرِ (ر ج ا، ر ج ي): الألفُ في الآخرِ منقلبةٌ عن واوٍ أو ياءٍ؛ ارجعْ إلى الثّلاثيِّ (رَجَوتُ ← ر ج و)",
 "Tu prends l'alif ou le ي visibles pour des lettres de la racine (ر ج ا، ر ج ي) : l'alif final vient d'un و ou d'un ي ; remonte au trilitère (رَجَوتُ ← ر ج و)",
 "You count the visible alif or ي as root letters (ر ج ا، ر ج ي): a final alif comes from و or ي; go back to the three-letter verb (رَجَوتُ ← ر ج و)")
mu('12','05#2:c',"« لِقاءٌ » pour un nom de lieu : `masdar-bada-al-mushtaqq` (6ᵉ) ne parle que du nom d'agent / de patient ; erreur isolée")
# ---------- 6. ch13 : tasghir ----------
ren('arabe.tasghir.ya-ba3d-al-thani-ta3rif','arabe.tasghir.sighat-al-tasghir-khalt',"même règle (damma + ي sukûn ; le ي long de فَعِيل n'est pas un diminutif) que `sighat-al-tasghir-khalt`, qui cite déjà أَبِيّ et جَبِيل ; 1 question.")
LABO['arabe.tasghir.sighat-al-tasghir-khalt']=(
 "تخطئُ في صيغةِ التّصغيرِ: ضمُّ الأوّلِ ثمّ ياءٌ ساكنةٌ بعدَ الثّاني (جُبَيْل)؛ فياءُ «فَعِيل» المدّيّةُ (أَمِين، الوَلِيد) والفتحُ والكسرُ لا تصنعُ تصغيرًا",
 "Tu reconnais ou formes mal le diminutif : damma sur la 1re lettre puis ي sukûn après la 2e (جُبَيْل) ; le ي long de فَعِيل (أَمِين), une fatha ou kasra n'en font pas",
 "You spot or build the diminutive wrongly: damma on the 1st letter, then ي with sukûn after the 2nd (جُبَيْل); the long ي of فَعِيل (أَمِين), a fatha or kasra make none")
# ---------- 7. fonction d'un groupe : verbe ou pas (A 16 + compléments 03) ----------
ren('arabe.istifham.markab-jarr-khabar-aw-mutammim','arabe.jumla.wazifa-bila-ta3alluq',"même règle que le piège n°1 de ch03 (« اسألْ عمّا يتعلّقُ به المركَّبُ: أفعلٌ هو أم مبتدأٌ ») : un seul id, domaine `jumla`.")
ren('arabe.zaman.wazifa-min-al-ma3na','arabe.jumla.wazifa-bila-ta3alluq',"(complément 03) fusionné avec l'id A de ch16 ; les options où la حال est en jeu passent à un id propre, `arabe.zaman.hal-wa-mafoul-fihi-khalt`.")
LABO['arabe.jumla.wazifa-bila-ta3alluq']=(
 "تحكمُ على وظيفةِ المركّبِ (جارٍّ ومجرورٍ أو ظرفٍ) بمعناه أو موضعِه دونَ أن تسألَ: أفي الجملةِ فعلٌ؟ معه متمّمٌ له، ودونَه خبرٌ وما بعدَه مبتدأٌ لا فاعلٌ",
 "Tu fixes la fonction d'un groupe (جارّ ومجرور، ظرف) par son sens ou sa place sans voir s'il y a un verbe : verbe → son متمّم ; sans verbe → خبر, le nom est مبتدأ",
 "You set a phrase's function (prepositional or adverbial) by meaning or place, not by asking if there is a verb: with one, it completes it; without, it is خبر, the noun مبتدأ")
NEWD['arabe.zaman.hal-wa-mafoul-fihi-khalt']=(
 "تفرّقُ بين الحالِ والمفعولِ فيه بالمعنى وقد يتقاربانِ: الشّكلُ يحسمُ: أداةُ زمنٍ (لمّا رأى، بعدَ أن) ← مفعولٌ فيه، وواوٌ وجملةٌ تصفُ الهيأةَ أو مضارعٌ ← حالٌ",
 "Tu distingues حال et مفعول فيه par le sens, parfois identique : la forme décide — outil de temps (لمّا رأى، بعد أن) → مفعول فيه ; و + phrase d'état ou مضارع → حال",
 "You tell حال from مفعول فيه by meaning, which may match: form decides — a time tool (لمّا رأى، بعدَ أن) → مفعول فيه; و + state clause or مضارع → حال")
rt('03','02#6:c 06#1:a 06#5:bcd 06#4:d quiz#2:c 05#4:d quiz#5:d','arabe.zaman.hal-wa-mafoul-fihi-khalt','la حال est en jeu (clé ou option)')
# ---------- 8. retouches d'exactitude ----------
rt('07','05#2:bcd','arabe.sura.tashbih-isti3ara-khalt',"« quel pilier peut tomber ? » : ôter un des deux termes fait une استعارة — c'est la règle de `tashbih-isti3ara-khalt`, pas un pilier mal nommé")
mu('06','04#1:d',"« le verbe de six lettres ne forme pas de nom de patient » : croyance fausse que `mazid-haraka-al-3ayn` (6ᵉ) ne dit pas")
mu('11','03#2:b quiz#4:bc',"`nawasikh.ism-khabar-maqlub` (6ᵉ) parle d'un خبر avancé (في البيت) suivi d'un nom indéfini : ce n'est pas le cas ici ; 2 questions, sous le seuil pour un id neuf")
mu('01','05#1:bc quiz#1:cd',"distracteurs absurdes (« المعربة تُنصب فقط… », « المعربة هي الحروف فقط ») : aucune erreur d'élève reconstructible (R1–R3)")
LABO['arabe.ishtiqaq.fa3il-mubalagha-wa-sifa']=(
 "تعدُّ «فَعِيلًا» أو «فَعُولًا» أو «فَعِلًا» صفةً مشبّهةً دائمًا (عَلِيم، غَيُور، حَذِر): هي من أوزانِ المبالغةِ أيضًا؛ الثّبوتُ ← صفةٌ مشبّهةٌ، وكثرةُ الحدثِ ← مبالغةٌ",
 "Tu ranges tout فَعِيل, فَعُول ou فَعِل parmi les صفات مشبّهة (عَلِيم، غَيُور، حَذِر) : ce sont aussi des intensifs ; stabilité → صفة مشبّهة, abondance → intensif",
 "You file every فَعِيل, فَعُول or فَعِل as a resembling adjective (عَلِيم، غَيُور، حَذِر): they are intensive patterns too; permanence → adjective, abundance → intensive")
LOG.append("`arabe.ishtiqaq.fa3il-mubalagha-wa-sifa` : libellé élargi à فَعِل (حَذِر), sinon l'option 06:04#2→b n'était pas dite (doute B-2).")
# ---------- libellés resserrés (≤ 160 caractères) ----------
LABO['arabe.jumla.ra2isi-bi-tartib-al-dhikr']=(LABO['arabe.jumla.ra2isi-bi-tartib-al-dhikr'][0],
 "Tu prends pour principal le fait dit en premier ou celui que mène l'outil : c'est celui de la phrase sans outil (حرف الشرط, أداة الزمن), où qu'elle soit",
 "You take as main the event said first or the one the tool introduces: it is the one in the clause without the tool (condition or time tool), wherever it is")
LABO['arabe.rabt.istidrak-khalt']=(LABO['arabe.rabt.istidrak-khalt'][0],
 "Tu vois un استدراك où il n'y en a pas, ou tu le manques : il dit le contraire de ce que la 1re phrase faisait attendre (لكنّ، غيرَ أنّ) ; ni contraste ni suite attendue",
 "You see an استدراك where there is none, or miss it: it says the opposite of what clause 1 led us to expect (لكنّ، غيرَ أنّ); not a contrast, not an expected result")
LABO['arabe.rabt.mu2ashshir-ghayr-munasib']=(
 "تخلطُ بين معاني المؤشّراتِ: التّعليلُ (لأنّ، إذ)، والنّتيجةُ (فـ، إذن، بناءً على ذلك)، والمهلةُ (ثمّ)، والتّفسيرُ (أي)، والتّقابلُ (بينما)، والإضافةُ (علاوةً)",
 LABO['arabe.rabt.mu2ashshir-ghayr-munasib'][1],LABO['arabe.rabt.mu2ashshir-ghayr-munasib'][2])
LABO['arabe.mazid.ma3na-bila-nazar-fil-jidhr']=(LABO['arabe.mazid.ma3na-bila-nazar-fil-jidhr'][0],
 "Tu donnes au schème un sens sans examiner racine ni phrase : un schème a plusieurs sens ; la racine (verbe, chose, lieu, couleur, qualité) et le contexte tranchent",
 "You give the pattern a meaning without checking root or sentence: a pattern has several; the root (verb, thing, place, colour, quality) and the context decide")
LABO['arabe.hijaj.mahdhuda-muthbata-khalt']=(LABO['arabe.hijaj.mahdhuda-muthbata-khalt'][0],
 "Tu confonds thèse réfutée (avis de l'adversaire, souvent dit en premier) et défendue (avis de l'auteur) : l'ordre ne décide pas ; cherche بل، والحقُّ أنّ، ليس",
 "You mix up the refuted thesis (the opponent's view, often said first) and the defended one (the author's): order decides nothing; look for بل، والحقُّ أنّ، ليس")
LABO['arabe.hijaj.taqsim-al-binya-khalt']=(LABO['arabe.hijaj.taqsim-al-binya-khalt'][0],
 "Tu découpes mal le texte : la thèse est un avis (réfutée + défendue ensemble s'il y en a deux) ; démarche = arguments et exemples ; la conclusion est à part",
 "You split the text wrongly: the thesis is a view (refuted + defended together if both); the path = arguments and examples; the conclusion stands apart")
LABO['arabe.tasghir.sighat-al-tasghir-khalt']=(LABO['arabe.tasghir.sighat-al-tasghir-khalt'][0],
 "Tu reconnais ou formes mal le diminutif : damma sur la 1re lettre, ي sukûn après la 2e (جُبَيْل) ; le ي long de فَعِيل (أَمِين), fatha ou kasra n'en font pas",
 "You spot or build the diminutive wrongly: damma on letter 1, ي with sukûn after letter 2 (جُبَيْل); the long ي of فَعِيل (أَمِين), a fatha or kasra make none")
LABO['arabe.jumla.wazifa-bila-ta3alluq']=(LABO['arabe.jumla.wazifa-bila-ta3alluq'][0],
 "Tu fixes la fonction d'un groupe (جارّ ومجرور، ظرف) par son sens ou sa place sans voir s'il y a un verbe : verbe → son متمّم ; sinon → خبر, le nom est مبتدأ",
 "You set a phrase's function by meaning or place without checking for a verb: with a verb it completes it; without, it is the خبر and the noun is the مبتدأ")
LABO['arabe.ishtiqaq.fa3il-mubalagha-wa-sifa']=(
 "تعدُّ «فَعِيلًا» أو «فَعُولًا» أو «فَعِلًا» صفةً مشبّهةً دائمًا (عَلِيم، غَيُور، حَذِر): هي أوزانُ مبالغةٍ أيضًا؛ الثّبوتُ ← صفةٌ مشبّهةٌ، والكثرةُ ← مبالغةٌ",
 "Tu ranges tout فَعِيل, فَعُول ou فَعِل parmi les صفات مشبّهة (عَلِيم، غَيُور، حَذِر) : ce sont aussi des intensifs ; stabilité → صفة, abondance → intensif",
 "You file every فَعِيل, فَعُول or فَعِل as a resembling adjective (عَلِيم، غَيُور، حَذِر): they are intensive patterns too; permanence → adjective, abundance → intensive")
NEWD['arabe.maqsur.radd-alif-bila-3add']=(NEWD['arabe.maqsur.radd-alif-bila-3add'][0],
 "Tu rends l'alif du maqsur au duel ou au pluriel sans compter : plus de 3 lettres → toujours ي (مُستشفيان، ذِكرَيات) ; 3 lettres → son origine (عَصَوان، هُديان)",
 NEWD['arabe.maqsur.radd-alif-bila-3add'][2])
NEWD['arabe.zaman.hal-wa-mafoul-fihi-khalt']=(NEWD['arabe.zaman.hal-wa-mafoul-fihi-khalt'][0],
 "Tu distingues حال et مفعول فيه par le sens, parfois le même : la forme décide — outil de temps (لمّا رأى، بعد أن) → مفعول فيه ; و + phrase d'état ou مضارع → حال",
 NEWD['arabe.zaman.hal-wa-mafoul-fihi-khalt'][2])
LABO['arabe.rabt.istidrak-khalt']=(LABO['arabe.rabt.istidrak-khalt'][0],
 "Tu vois un استدراك où il n'y en a pas, ou le manques : il dit le contraire de ce que la 1re phrase faisait attendre (لكنّ، غيرَ أنّ), ni contraste ni suite attendue",
 "You see an استدراك where there is none, or miss it: it says the opposite of what clause 1 made us expect (لكنّ، غيرَ أنّ); not a contrast nor an expected result")
LABO['arabe.mazid.ma3na-bila-nazar-fil-jidhr']=(LABO['arabe.mazid.ma3na-bila-nazar-fil-jidhr'][0],
 "Tu donnes au schème un sens sans voir racine ni phrase : un schème a plusieurs sens ; la racine (verbe, chose, lieu, couleur, qualité) et le contexte tranchent",
 LABO['arabe.mazid.ma3na-bila-nazar-fil-jidhr'][2])
LABO['arabe.ishtiqaq.fa3il-mubalagha-wa-sifa']=(LABO['arabe.ishtiqaq.fa3il-mubalagha-wa-sifa'][0],LABO['arabe.ishtiqaq.fa3il-mubalagha-wa-sifa'][1],
 "You file every فَعِيل, فَعُول or فَعِل as a resembling adjective (عَلِيم، غَيُور، حَذِر): they are intensives too; permanence → adjective, abundance → intensive")
LABO['arabe.rabt.istidrak-khalt']=(LABO['arabe.rabt.istidrak-khalt'][0],
 "Tu vois un استدراك où il n'y en a pas, ou le manques : il dit le contraire de ce que la 1re phrase faisait attendre (لكنّ، غيرَ أنّ) ; pas un contraste (بينما)",
 LABO['arabe.rabt.istidrak-khalt'][2])
rt('09','05#1:d','arabe.sard.nihaya-hors-nihaya',"« عادَ الهدوءُ… » (état final) pris pour le حدث قادح : libellé 6ᵉ exact")
rt('09','05#1:b','arabe.sard.3ada-hors-bidaya',"« كانَ الحيُّ نائمًا » (situation initiale) pris pour le حدث قادح : libellé 6ᵉ exact")
