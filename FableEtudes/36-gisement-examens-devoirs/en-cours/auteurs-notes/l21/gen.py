# -*- coding: utf-8 -*-
import json, math, sys
sys.path.insert(0,'/tmp/claude-0/-home-user/b03814da-e5f9-5a74-bf03-e7c23b20207a/scratchpad/l21-work')
from svglib import *
OUT='/home/user/wt-m21/content/math/09-triangle-rectangle-trigo/exercices/'
LETTERS='abcd'
def Q(prompt, opts, key, expl, diff, comp, fig=None):
    # opts: list of (text, tag|None) in display order ; key: index
    assert 0<=key<4 and len(opts)==4
    p=prompt+("\n"+fig if fig else "")
    o=[]
    for i,(t,tag) in enumerate(opts):
        d={"id":LETTERS[i],"text":t}
        if tag: d["misconceptionTag"]=tag
        o.append(d)
    return {"prompt":p,"options":o,"correctOption":LETTERS[key],"explanation":expl,"difficulty":diff,"competencies":[comp]}
DIFFS={47:[1,1,2,3],48:[1,1,2,2,2,2,3],49:[1,1,2,2],50:[1,1,1,2,2,3,3],51:[1,1,2,2,2,2]}
TARGET={50:"cadbabc",51:"cabdac"}
def rot(q,k):
    o=q["options"]; ki=LETTERS.index(q["correctOption"])
    sh=(ki-k)%4
    o=o[sh:]+o[:sh]
    for i,x in enumerate(o): x["id"]=LETTERS[i]
    q["options"]=o; q["correctOption"]=LETTERS[k]
def write(name,title,diff,mode,xp,coins,order,qs):
    if order in TARGET:
        for q,t in zip(qs,TARGET[order]): rot(q,LETTERS.index(t))
    for q,dd in zip(qs,DIFFS[order]): q["difficulty"]=dd
    d={"title":title,"difficulty":diff,"mode":mode,"xpReward":xp,"rewardCoins":coins,"displayOrder":order,"questions":qs}
    json.dump(d,open(OUT+name,'w'),ensure_ascii=False,indent=2); open(OUT+name,'a').write("\n")
    print(name,len(qs))
NB=' '

# ---------------------------------------------------------------- 47
def fig47_tri():
    A=(56,40);B=(184,40);C=(56,136)
    b=poly([A,B,C])+rightangle(A,B,C)+dots([A,B,C])+labels([("A",40,34),("B",198,34),("C",42,152)])+dim([("8 cm",120,30),("6 cm",30,92)])
    return svg(240,170,"المثلّث ABC القائم في A وطولا الضلعين AB و AC",b)
def fig47_semi():
    A=(56,40);B=(184,40);C=(56,136);I=(120,88)
    arc='<path d="M%d %d A80 80 0 0 1 %d %d" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linecap="round"/>'%(B[0],B[1],C[0],C[1])
    b=poly([A,B,C],fill=False)
    b=('<polygon points="56,40 184,40 56,136" fill="#0f172a" fill-opacity="0.04"/>'
       '<path d="M56 40 L184 40" fill="none" stroke="#0f172a" stroke-width="2.2" stroke-linecap="round"/>'
       '<path d="M56 40 L56 136" fill="none" stroke="#0f172a" stroke-width="2.2" stroke-linecap="round"/>'
       +seg(B,C,GREY,2.2,True)+arc+rightangle(A,B,C)+dots([A,B,C,I])
       +labels([("A",40,34),("B",198,34),("C",42,152),("I",I[0]-12,I[1]-6)])
       +dim([("8 cm",120,30),("6 cm",30,92)]))
    return svg(240,190,"المثلّث ABC القائم في A ونصف الدائرة التي قطرها BC",b)
q47=[]
q47.append(Q("إذا كان اللتر الواحد من الحليب يحتوي على 10 g من الزبدة ، فما كمّية الحليب اللازمة للحصول على 1500 g من الزبدة ، باللتر ؟",
 [("15","math.num.puissance-de-dix-rangs-mal-comptes"),("150",None),("1500","math.prop.pourcentage-recopie-comme-resultat"),("15"+NB+"000","math.num.operation-inverse-appliquee")],1,
 "كلّ لتر يعطي 10 g من الزبدة ، فعدد اللترات اللازمة هو عدد المرّات التي يتّسع فيها 10 g داخل 1500 g ، أي 1500 ÷ 10 = 150 ℓ ✓. الخطأ الشائع: القسمة على 100 بدل 10 فنجد 15 ؛ أو نقل العدد 1500 من الإعطاء كما هو ، مع أنّه كتلة الزبدة لا كمّية الحليب ؛ أو الضرب بدل القسمة فنجد 1500 × 10 = 15 000.",1,"math.prop.situations"))
q47.append(Q("ليكن x = −1.\nما القيمة العدديّة للعبارة التالية ؟\nA = (x − 2)x",
 [("−3","math.int.produit-signes-negatifs"),("−1","math.int.produit-signes-negatifs"),("1",None),("3",None)],3,
 "نعوّض x بالعدد −1 في العاملين: x − 2 = −1 − 2 = −3 ، ثمّ نضرب في x = −1 ، فنجد A = (−3) × (−1) = 3 ✓ ، لأنّ جداء عددين سالبين موجب. الخطأ الشائع: كتابة (−3) × (−1) = −3 بإهمال قاعدة الإشارات ؛ أو نشر العبارة إلى x² − 2x ثمّ الخطأ في إشارة الجداء −2 × (−1) فنجد 1 − 2 = −1 ؛ أو إهمال القوسين وحساب x − 2x فنجد −1 + 2 = 1.",1,"math.num.relatifs-operations"))
q47.append(Q("في الشكل التالي ، المثلّث ABC قائم في A ، ونعلم أنّ الأطوال بالصنتمتر هي:\nAB = 8\nAC = 6\nما طول القطعة [BC] بالصنتمتر ؟",
 [("2√7","math.geo.hypotenuse-mal-choisie"),("10",None),("√14","math.geo.pythagore-sans-carres"),("28",None)],1,
 "المثلّث ABC قائم في A ، فوتره [BC] ، وبنظرية فيثاغورس BC² = AB² + AC² = 64 + 36 = 100 ، إذن BC = √100 = 10 cm ✓. الخطأ الشائع: جمع الطولين تحت الجذر بلا تربيع فنجد BC = √(8 + 6) = √14 ؛ أو اعتبار [AB] وترًا فنجد BC² = 64 − 36 = 28 أي BC = √28 = 2√7 ، أو التوقّف عند هذا المربّع 28.",2,"math.geo.pythagore",fig47_tri()))
q47.append(Q("في الشكل التالي ، المثلّث ABC قائم في A ، ونعلم أنّ الأطوال بالصنتمتر هي:\nAB = 8\nAC = 6\nألصقنا بالمثلّث ، على ضلعه [BC] ومن خارجه ، نصف قرص قطره [BC] ومركزه I.\nما قيس محيط الشكل الناتج بالصنتمتر ؟",
 [("14 + 10π",None),("24 + 10π",None),("14 + 5π",None),("24 + 5π",None)],2,
 "نحسب أوّلاً القطر: BC² = AB² + AC² = 64 + 36 = 100 ، إذن BC = 10 ، ونصف القطر IB = 5. طول قوس نصف الدائرة هو نصف محيط الدائرة: (2 × π × 5) ÷ 2 = 5π. حدّ الشكل الناتج يتكوّن من [AB] و [AC] والقوس ، أمّا القطعة [BC] فصارت داخله ، فمحيطه 8 + 6 + 5π = 14 + 5π ✓. الخطأ الشائع: إضافة القطر [BC] وهو صار داخل الشكل وليس من حدّه فنجد 24 + 5π ؛ أو أخذ محيط الدائرة كاملة 2 × π × 5 = 10π بدل نصفه فنجد 14 + 10π.",3,"math.mes.perimetres",fig47_semi()))
write("47-examen-2019-technique-ex1-qcm-proportion-valeur-numerique-pythagore-perimetre-demi-cercle.json",
 "🏛️ مناظرة 2019 (تقني) · التمرين 1 ⭐⭐: اختيار من متعدّد — تناسب وقيمة عدديّة وفيثاغورس ومحيط شكل بنصف دائرة",2,"practice",75,15,47,q47)

# ---------------------------------------------------------------- 48
def tri48(H=False, lab=(), shade=None, marks=()):
    A=(60,184);B=(180,184);C=(60,24)
    t=0.36
    Hp=(B[0]+t*(C[0]-B[0]),B[1]+t*(C[1]-B[1]))
    b=poly([A,B,C])
    if shade: b+=poly([A,B,Hp],op=0.12)
    if H:
        b+=seg(A,Hp,GREEN,2.8)+rightangle(Hp,A,B if False else C)
    b+=rightangle(A,B,C)
    pts=[A,B,C]+([Hp] if H else [])
    b+=dots(pts)
    L=[("A",44,202),("B",194,202),("C",60,14)]
    if H: L.append(("H",Hp[0]+14,Hp[1]-2))
    b+=labels(L)
    D=[]
    if 'AC' in lab: D.append(("4 cm",32,108))
    if 'AB' in lab: D.append(("3 cm",120,204))
    b+=dim(D)
    return svg(230,214,"المثلّث ABC القائم في A",b),A,B,C,Hp
def tri_abh(lab):
    A=(60,184);B=(180,184);C=(60,24)
    Hp=(B[0]+0.36*(C[0]-B[0]),B[1]+0.36*(C[1]-B[1]))
    b=poly([A,B,Hp],op=0.08)+rightangle(Hp,A,B)+dots([A,B,Hp])+labels([("A",44,202),("B",194,202),("H",Hp[0]+14,Hp[1]-4)])
    D=[]
    if 'AB' in lab: D.append(("3 cm",120,204))
    if 'AH' in lab: D.append(("2,4 cm",(A[0]+Hp[0])/2-16,(A[1]+Hp[1])/2-20))
    if 'HB' in lab: D.append(("1,8 cm",(Hp[0]+B[0])/2+24,(Hp[1]+B[1])/2-14))
    b+=dim(D)
    return svg(230,214,"المثلّث ABH القائم في H",b)
f48_1=tri48()[0]
f48_2=tri48(lab=('AB','AC'))[0]
f48_3=tri48(H=True)[0]
f48_4=tri48(H=True,lab=('AB','AC'))[0]
q48=[]
q48.append(Q("يمثّل التصميم التالي قطعة أرض على شكل مثلّث ABC قائم في A ، ونريد إكمال المساواة:\nBC² = … + AC²\nأيّ إكمال صحيح ، مع تبريره ؟",
 [("نظرية فيثاغورس ، والحدّ الناقص هو AB",'math.geo.pythagore-sans-carres'),("عكس نظرية فيثاغورس ، والحدّ الناقص هو AB",None),("نظرية فيثاغورس ، والحدّ الناقص هو AB²",None),("عكس نظرية فيثاغورس ، والحدّ الناقص هو AB²",'math.geo.pythagore-reciproque-role')],2,
 "المثلّث ABC قائم في A ، فوتره [BC] ، والزاوية القائمة معلومة ، فنطبّق نظرية فيثاغورس المباشرة: BC² = AB² + AC² ✓ ، والمساواة تربط مربّعات الأطوال لا الأطوال نفسها. الخطأ الشائع: استعمال عكس النظرية ، وهي تُثبت أنّ المثلّث قائم انطلاقًا من أطوال أضلاعه ، ولا تُستعمل حين تكون الزاوية القائمة معلومة ؛ أو كتابة AB بدل AB² فتصير المساواة مجموعًا للأطوال.",1,"math.geo.pythagore",f48_1))
q48.append(Q("يمثّل التصميم التالي قطعة أرض على شكل مثلّث ABC قائم في A ، ونعلم أنّ الأطوال على التصميم بالسنتمتر هي:\nAB = 3\nAC = 4\nما طول القطعة [BC] على التصميم بالسنتمتر ؟",
 [("√7","math.geo.hypotenuse-mal-choisie"),("5",None),("√12",None),("49",None)],1,
 "المثلّث ABC قائم في A ، فوتره [BC] ، وبنظرية فيثاغورس BC² = AB² + AC² = 9 + 16 = 25 ، إذن BC = √25 = 5 cm ✓. الخطأ الشائع: عدّ [AC] وترًا فنجد BC² = 16 − 9 = 7 أي BC = √7 ؛ أو ضرب الطولين تحت الجذر فنجد √(3 × 4) = √12 ؛ أو تربيع مجموعهما فنجد (3 + 4)² = 49.",1,"math.geo.pythagore",f48_2))
q48.append(Q("في قطعة أرض على شكل مثلّث ABC قائم في A ، النقطة H من القطعة [BC] حيث (AH) ⟂ (BC).\nنريد تبرير المساواة التالية:\nAH × BC = AB × AC\nأيّ تعليل صحيح ؟",
 [("مساحة المثلّث ABC تساوي BC × AH ÷ 2 وتساوي أيضًا BC × AC ÷ 2",None),("مساحة المثلّث ABC تساوي AB × AH ÷ 2 وتساوي أيضًا AB × AC ÷ 2","math.geo.relation-aire-mauvais-cote"),("مساحة المثلّث ABC تساوي AB × AH ÷ 2 وتساوي أيضًا BC × AC ÷ 2",None),("مساحة المثلّث ABC تساوي BC × AH ÷ 2 وتساوي أيضًا AB × AC ÷ 2",None)],3,
 "نحسب مساحة المثلّث ABC بطريقتين. بالقاعدة [BC] وارتفاعها [AH] لأنّ (AH) ⟂ (BC) تكون المساحة:\nBC × AH ÷ 2\nوبالقاعدة [AB] وارتفاعها [AC] لأنّ المثلّث قائم في A تكون المساحة:\nAB × AC ÷ 2\nالمساحة واحدة ، فنساوي الحسابين ونضرب في 2 فنجد:\nAH × BC = AB × AC\nوهذا هو المطلوب ✓\n الخطأ الشائع: ضرب الارتفاع [AH] في ضلع من ضلعي الزاوية القائمة ، مع أنّ [AH] ارتفاع الوتر [BC] لا ارتفاع [AB] ؛ أو اعتبار [AC] ارتفاعًا للقاعدة [BC] ، وهو ليس عموديًّا عليها.",2,"math.geo.relations-metriques",f48_3))
q48.append(Q("في قطعة أرض على شكل مثلّث ABC قائم في A ، النقطة H من القطعة [BC] حيث (AH) ⟂ (BC) ، ونعلم أنّ الأطوال بالسنتمتر هي:\nAB = 3\nAC = 4\nما طول القطعة [AH] بالسنتمتر ؟",
 [("2,4",None),("2,5","math.geo.hauteur-confondue-avec-mediane"),("12/7","math.geo.pythagore-sans-carres"),("0,48","math.geo.pythagore-racine-oubliee")],0,
 "نحسب أوّلًا الوتر بنظرية فيثاغورس: BC² = AB² + AC² = 9 + 16 = 25 ، إذن BC = 5. ثمّ نحسب مساحة المثلّث ABC بطريقتين: AH × BC = AB × AC ، أي AH × 5 = 3 × 4 = 12 ، ومنه AH = 12 ÷ 5 = 2,4 cm ✓. الخطأ الشائع: اعتبار [AH] ميانة فنجد نصف الوتر 5 ÷ 2 = 2,5 ، مع أنّ H ليس منتصف [BC] ؛ أو جمع الضلعين بدل مربّعيهما فنأخذ BC = 3 + 4 = 7 ونجد AH = 12/7 ؛ أو القسمة على BC² = 25 بدل BC = 5 فنجد 12 ÷ 25 = 0,48.",2,"math.geo.relations-metriques",f48_4))
q48.append(Q("المثلّث ABH قائم في H ، ونعلم أنّ الأطوال بالسنتمتر هي:\nAB = 3\nAH = 2,4\nما طول القطعة [HB] بالسنتمتر ؟",
 [("0,6","math.geo.pythagore-sans-carres"),("1,8",None),("5,4","math.geo.pythagore-sans-carres"),("√14,76","math.geo.hypotenuse-mal-choisie")],1,
 "المثلّث ABH قائم في H ، فوتره [AB] ، وبنظرية فيثاغورس AB² = AH² + HB² ، أي 9 = 5,76 + HB² ، ومنه HB² = 9 − 5,76 = 3,24 ، إذن HB = √3,24 = 1,8 cm ✓. الخطأ الشائع: طرح الطولين مباشرة فنجد 3 − 2,4 = 0,6 ، أو جمعهما فنجد 3 + 2,4 = 5,4 ؛ أو عدّ [AB] ضلعًا قائمًا فنجد HB² = 9 + 5,76 = 14,76.",3,"math.geo.pythagore",tri_abh(('AB','AH'))))
q48.append(Q("المثلّث ABH قائم في H ، ونعلم أنّ الأطوال على التصميم بالسنتمتر هي:\nHB = 1,8\nAH = 2,4\nما مساحة المثلّث ABH على التصميم بالسنتمتر المربّع ؟",
 [("2,16",None),("3,6",None),("4,2","math.mes.aire-et-perimetre-confondus"),("4,32","math.mes.aire-triangle-sans-moitie")],0,
 "المثلّث ABH قائم في H ، فضلعاه القائمان [HB] و [AH] أحدهما قاعدة والآخر ارتفاع ، ومساحته HB × AH ÷ 2 = 1,8 × 2,4 ÷ 2 = 4,32 ÷ 2 = 2,16 cm² ✓. الخطأ الشائع: نسيان القسمة على 2 فنجد 4,32 ؛ أو جمع الطولين كما في المحيط فنجد 1,8 + 2,4 = 4,2 ؛ أو ضرب الوتر [AB] في [AH] ثمّ القسمة على 2 فنجد 3 × 2,4 ÷ 2 = 3,6 ، مع أنّ [AB] ليس عموديًّا على [AH].",2,"math.mes.aires",tri_abh(('AH','HB'))))
q48.append(Q("رُسمت قطعة أرض على تصميم سلّمه 1/1000 ، أي أنّ كلّ 1 cm على التصميم يمثّل 1000 cm في الواقع. جزؤها الأوّل مثلّث ABH قائم في H ، وطولا ضلعيه القائمين على التصميم بالسنتمتر هما:\nHB = 1,8\nAH = 2,4\nما المساحة الحقيقيّة لهذا الجزء بالمتر المربّع ؟",
 [("0,216","math.mes.echelle-aire-rapport-non-carre"),("21,6","math.mes.echelle-aire-rapport-non-carre"),("216",None),("2160",None)],2,
 "على التصميم تساوي مساحة المثلّث ABH:\n1,8 × 2,4 ÷ 2 = 2,16\nأي 2,16 سنتمتر مربّع. كلّ 1 cm على التصميم يمثّل 1000 cm في الواقع ، أي 10 m ، فكلّ سنتمتر مربّع على التصميم هو مربّع ضلعه 10 أمتار ، ومساحته:\n10 × 10 = 100\nأي 100 متر مربّع. إذن المساحة الحقيقيّة:\n2,16 × 100 = 216\nأي 216 مترًا مربّعًا ✓.\n الخطأ الشائع: تطبيق نسبة الأطوال على المساحة دون تربيعها: الضرب في 10 فنجد 21,6 ، أو الضرب في 1000 ثمّ التحويل إلى المتر المربّع بالقسمة على 10 000 فنجد 0,216 ؛ أو ضرب 2,16 في 1000 دون تربيع ثمّ الاكتفاء بهذا العدد مترًا مربّعًا فنجد 2160.",3,"math.mes.aires",None))
write("48-examen-2020-technique-ex3-terrain-triangle-pythagore-hauteur-aire-echelle.json",
 "🏛️ مناظرة 2020 (تقني) · التمرين 3 ⭐⭐⭐: قطعة أرض مقسّمة — فيثاغورس والارتفاع والمساحة والسلّم",3,"boss",120,30,48,q48)

# ---------------------------------------------------------------- 49
q49=[]
q49.append(Q("احسب ثمّ اختصر الناتج:\n√2 × (√8 − √2)",
 [("2",None),("2√3","math.num.racine-distribuee-sur-somme"),("4 − √2","math.alg.distribution-partielle"),("2√2",None)],0,
 "نوزّع √2 على الحدّين: √2 × √8 − √2 × √2 = √16 − 2 = 4 − 2 = 2 ✓. طريقة ثانية: √8 = 2√2 ، فالقوس يساوي 2√2 − √2 = √2 ، وجداء √2 في √2 يساوي 2. الخطأ الشائع: دمج √8 − √2 في √6 فنجد √2 × √6 = √12 = 2√3 ؛ أو ضرب √2 في الحدّ الأوّل فقط فنجد 4 − √2.",2,"math.num.racines-calcul"))
q49.append(Q("ما مقابل العدد التالي ؟\n1 − √3",
 [("−1 − √3","math.alg.moins-devant-parenthese"),("1 + √3","math.alg.moins-devant-parenthese"),("√3 − 1",None),("1/(1 − √3)","math.num.oppose-inverse-confondus")],2,
 "مقابل عدد هو العدد الذي يجمع معه صفرًا ، وهو يغيّر إشارة كلّ حدّ: −(1 − √3) = −1 + √3 = √3 − 1 ✓ ، وفعلًا (1 − √3) + (√3 − 1) = 0. الخطأ الشائع: تغيير إشارة حدّ واحد فقط فنجد −1 − √3 أو 1 + √3 ؛ أو أخذ المقلوب بدل المقابل فنجد 1/(1 − √3).",1,"math.num.racines-calcul"))
q49.append(Q("ما قيمة العدد التالي ؟\n|1 − √2| − √2",
 [("−1",None),("1",None),("1 − 2√2","math.num.valeur-absolue-signe-du-contenu-non-teste"),("2√2 − 1","math.num.operation-inverse-appliquee")],0,
 "√2 أكبر من 1 لأنّ 2 أكبر من 1 ، فالعدد 1 − √2 سالب ، وقيمته المطلقة هي مقابله: |1 − √2| = √2 − 1. إذن |1 − √2| − √2 = √2 − 1 − √2 = −1 ✓. الخطأ الشائع: رفع الشريطين دون اختبار الإشارة فنجد (1 − √2) − √2 = 1 − 2√2 ؛ أو جمع √2 بدل طرحه فنجد (√2 − 1) + √2 = 2√2 − 1.",2,"math.num.valeur-absolue"))
q49.append(Q("ABC مثلّث قائم في A ، ونعلم أنّ الأطوال بالمتر هي:\nAB = 40\nBC = 50\nما طول القطعة [AC] بالمتر ؟",
 [("10","math.geo.pythagore-sans-carres"),("30",None),("900","math.geo.pythagore-racine-oubliee"),("√4100","math.geo.hypotenuse-mal-choisie")],1,
 "المثلّث ABC قائم في A ، فوتره [BC] ، وبنظرية فيثاغورس BC² = AB² + AC² ، أي 2500 = 1600 + AC² ، ومنه AC² = 2500 − 1600 = 900 ، إذن AC = √900 = 30 m ✓. الخطأ الشائع: طرح الطولين مباشرة فنجد 50 − 40 = 10 ؛ أو التوقّف عند AC² = 900 ؛ أو جمع المربّعين كأنّ [BC] ضلع قائم فنجد AC² = 1600 + 2500 = 4100.",2,"math.geo.pythagore"))
write("49-examen-2021-technique-ex1-qcm-radicaux-oppose-valeur-absolue-cote-manquant.json",
 "🏛️ مناظرة 2021 (تقني) · التمرين 1 ⭐⭐: اختيار من متعدّد — جذور تربيعيّة ومقابل عدد وقيمة مطلقة وضلع في مثلّث قائم",2,"practice",75,15,49,q49)

# ---------------------------------------------------------------- 50
def fig50(full=True, lab=()):
    B=(170,200);S=(170,50);A=(107.5,200);N=(170,155);M=(126.25,155)
    b=''
    # mur hachure
    for y in range(60,200,14):
        b+=seg((172,y+12),(186,y),GREY,1.4)
    b+=seg(S,B,INK,3.0)
    b+=seg(A,B,GREY,2.2,True)
    b+=seg(A,S,INK,2.2)
    if full:
        b+=seg(M,N,GREEN,2.8)+rightangle(N,M,S)
    b+=rightangle(B,A,S)+dots([A,B,S]+([M,N] if full else []))
    L=[("S",170,38),("B",184,216),("A",100,218)]
    if full: L+=[("N",158,174),("M",114,150)]
    b+=labels(L)
    D=[]
    if 'AB' in lab: D.append(("2,5 m",138,216))
    if 'BS' in lab: D.append(("6 m",206,128))
    b+=dim(D)
    return svg(240,230,"دعامة تثبّت حائطًا: المثلّثان ABS و MNS",b)
q50=[]
q50.append(Q("في دعامة تثبّت حائطًا أثريًّا ، المثلّث ABS قائم في B والمثلّث MNS قائم في N ، والنقطة M من [AS] والنقطة N من [SB].\nنريد كتابة المساواة التالية:\nAS² = BA² + BS²\nأيّ إكمال صحيح للتعليل ؟",
 [("نطبّق نظرية فيثاغورس على المثلّث ABS",None),("نطبّق عكس نظرية فيثاغورس على المثلّث ABS","math.geo.pythagore-reciproque-role"),("نطبّق نظرية فيثاغورس على المثلّث MNS","math.geo.segment-mal-choisi"),("نطبّق عكس نظرية فيثاغورس على المثلّث MNS",None)],0,
 "في المساواة AS² = BA² + BS² يقف مربّع [AS] وحده في طرف ، فـ [AS] هو الوتر ، أي الضلع المقابل للزاوية القائمة عند B. فنطبّق نظرية فيثاغورس المباشرة على المثلّث ABS القائم في B ✓. الخطأ الشائع: الاستناد إلى المثلّث MNS ، ووتره [MS] لا [AS] ؛ أو استعمال العكس ، وهو يُثبت أنّ مثلّثًا قائم انطلاقًا من أطواله ، ولا يُستعمل والزاوية القائمة معلومة.",1,"math.geo.pythagore",fig50(True)))
q50.append(Q("في دعامة تثبّت حائطًا أثريًّا ، المثلّث ABS قائم في B ، ونعلم أنّ الأطوال بالمتر هي:\nAB = 2,5\nBS = 6\nما طول القطعة [AS] بالمتر ؟",
 [("6,5",None),("8,5","math.geo.pythagore-sans-carres"),("42,25","math.geo.pythagore-racine-oubliee"),("√29,75","math.geo.hypotenuse-mal-choisie")],0,
 "المثلّث ABS قائم في B ، فوتره [AS] ، وبنظرية فيثاغورس AS² = AB² + BS² = 6,25 + 36 = 42,25 ، إذن AS = √42,25 = 6,5 m ✓. الخطأ الشائع: الجمع المباشر 2,5 + 6 = 8,5 ؛ أو التوقّف عند AS² = 42,25 ؛ أو عدّ [BS] وترًا فنجد AS² = 36 − 6,25 = 29,75.",2,"math.geo.pythagore",fig50(False,('AB','BS'))))
q50.append(Q("في دعامة تثبّت حائطًا أثريًّا ، المثلّث ABS قائم في B والمثلّث MNS قائم في N ، والنقطة M من [AS] والنقطة N من [SB].\nما العلاقة بين المستقيمين (MN) و (AB) ، وما تعليلها ؟",
 [("متوازيان ، لأنّ كلًّا منهما عمودي على (SB)",None),("متعامدان ، لأنّ كلًّا منهما عمودي على (SB)","math.geo.regle-perpendiculaire-parallele-inversee"),("متوازيان ، لأنّ المثلّثين ABS و MNS قائمان",None),("متعامدان ، لأنّ المثلّثين ABS و MNS قائمان",None)],0,
 "المثلّث ABS قائم في B ، فالمستقيم (AB) عمودي على (SB). والمثلّث MNS قائم في N ، فالمستقيم (MN) عمودي على (SB). وكلّ مستقيمين عموديين على مستقيم واحد متوازيان ، إذن (MN) ∥ (AB) ✓ ، وهذا التوازي شرط تطبيق نظرية طاليس. الخطأ الشائع: الاستنتاج أنّ المستقيمين متعامدان ، والصواب أنّ العموديّين على مستقيم واحد متوازيان ؛ أو الاكتفاء بأنّ المثلّثين قائمان ، فهذا وحده لا يربط (MN) بـ (AB) ما لم نذكر المستقيم الذي يعمدانه معًا.",2,"math.geo.droites-perp-para",fig50(True)))
q50.append(Q("في دعامة تثبّت حائطًا أثريًّا ، المستقيمان (MN) و (AB) متوازيان ، والنقطة M من [SA] والنقطة N من [SB].\nأيّ سلسلة مساواة بين النسب صحيحة بنظرية طاليس ؟",
 [("SM/SA = SN/SB = MN/AB",None),("SA/SM = SB/SN = MN/AB","math.geo.thales-rapport-inverse"),("SM/MA = SB/SN = AB/MN","math.geo.thales-formes-melangees"),("SA/SM = SN/NB = AB/MN","math.geo.thales-formes-melangees")],0,
 "(MN) ∥ (AB) والنقطتان M و N من [SA] و [SB] ، فبنظرية طاليس في المثلّث SAB: كلّ نسبة تقابل طولًا من المثلّث الصغير SMN بطوله المقابل في المثلّث الكبير SAB ، أي SM/SA = SN/SB = MN/AB ✓. الخطأ الشائع: قلب نسبتين وترك الثالثة على حالها ، والنسب الثلاث تُقلب معًا أو لا تُقلب ؛ أو إدخال نسبة الجزء على الباقي (SM/MA أو SN/NB) في سلسلة نسب الكلّ على الجزء.",2,"math.geo.thales-direct",fig50(True)))
q50.append(Q("على حائط أثري تتّصل دعامة بالنقطتين B و S ، والنقطة N من القطعة [SB]. نعلم أنّ الأطوال بالمتر هي:\nBS = 6\nBN = 1,8\nما طول القطعة [SN] بالمتر ؟",
 [("1,8","math.geo.segment-mal-choisi"),("4,2",None),("7,8","math.num.operation-inverse-appliquee"),("10,8",None)],1,
 "N من القطعة [SB] ، فـ [SB] تتكوّن من [SN] و [NB] ، أي SB = SN + NB ، ومنه SN = SB − BN = 6 − 1,8 = 4,2 m ✓. الخطأ الشائع: إعطاء القطعة المعلومة BN نفسها بدل القطعة الباقية ؛ أو الجمع 6 + 1,8 = 7,8 ؛ أو الضرب 6 × 1,8 = 10,8.",1,"math.geo.thales-direct",fig50(True)))
q50.append(Q("في دعامة تثبّت حائطًا أثريًّا ، المستقيمان (MN) و (AB) متوازيان ، والنقطة M من [SA] والنقطة N من [SB] ، ونعلم أنّ الأطوال بالمتر هي:\nSB = 6\nBN = 1,8\nAB = 2,5\nما طول القطعة [MN] بالمتر ؟",
 [("0,75","math.geo.segment-mal-choisi"),("1,75",None),("10,5","math.alg.coefficient-non-divise"),("25/7","math.geo.thales-rapport-inverse")],1,
 "نحسب أوّلًا SN = SB − BN = 6 − 1,8 = 4,2. وبنظرية طاليس SN/SB = MN/AB ، أي 4,2/6 = MN/2,5 ، ومنه MN = 4,2 × 2,5 ÷ 6 = 10,5 ÷ 6 = 1,75 m ✓. الخطأ الشائع: وضع BN مكان SN في النسبة فنجد 1,8 × 2,5 ÷ 6 = 0,75 ؛ أو التوقّف عند الجداء 4,2 × 2,5 = 10,5 دون قسمة ؛ أو قلب النسبة فنجد 2,5 × 6 ÷ 4,2 = 25/7.",3,"math.geo.thales-direct",fig50(True)))
q50.append(Q("في دعامة تثبّت حائطًا أثريًّا ، المثلّث ABS قائم في B ، والنقطة M من القطعة [AS] ، ونعلم أنّ الأطوال بالمتر هي:\nAB = 2,5\nBS = 6\nAM = 1,95\nما طول القطعة [SM] بالمتر ؟",
 [("1,95","math.geo.segment-mal-choisi"),("4,05","math.geo.segment-mal-choisi"),("4,55",None),("8,45","math.num.operation-inverse-appliquee")],2,
 "نحسب أوّلًا الوتر [AS] بنظرية فيثاغورس في المثلّث ABS القائم في B: AS² = AB² + BS² = 6,25 + 36 = 42,25 ، إذن AS = 6,5 m. وM من القطعة [AS] ، فـ AS = AM + MS ، ومنه SM = AS − AM = 6,5 − 1,95 = 4,55 m ✓. الخطأ الشائع: إعطاء القطعة المعلومة AM نفسها ؛ أو طرح AM من BS بدل AS فنجد 6 − 1,95 = 4,05 ؛ أو جمع الطولين فنجد 6,5 + 1,95 = 8,45.",3,"math.geo.pythagore",fig50(True,())))
q50=[q50[i] for i in (0,1,4,2,3,5,6)]
write("50-examen-2021-technique-ex3-support-mur-pythagore-parallelisme-thales-longueur.json",
 "🏛️ مناظرة 2021 (تقني) · التمرين 3 ⭐⭐⭐: دعامة لحائط أثري — فيثاغورس والتوازي وطاليس",3,"boss",120,30,50,q50)

# ---------------------------------------------------------------- 51
def fig51(full=True, lab=()):
    C=(30,20);A=(174,20);D=(126,20);B=(30,236);E=(126,92)
    b=poly([A,B,C],op=0.03) if False else ''
    b+=seg(C,A,INK,2.2)+seg(C,B,INK,2.2)+seg(A,B,INK,2.2)+seg(D,E,GREEN,2.8)
    b+=rightangle(C,A,B)+rightangle(D,A,E)+dots([C,A,D,B,E])
    b+=labels([("C",16,16),("A",188,16),("D",126,10),("B",16,252),("E",142,102)])
    return svg(220,262,"الشكل: (CA) و (CB) متعامدان ، و [DE] عمودي على (CA)",b)
def fig51_ade(lab=()):
    A=(174,20);D=(126,20);E=(126,92)
    b=poly([A,D,E],op=0.06)+rightangle(D,A,E)+dots([A,D,E])+labels([("A",188,16),("D",118,14),("E",118,108)])
    D2=[]
    if 'AD' in lab: D2.append(("2 cm",150,12))
    if 'DE' in lab: D2.append(("3 cm",104,60))
    b+=dim(D2)
    return svg(220,124,"المثلّث ADE القائم في D",b)
q51=[]
q51.append(Q("المثلّث ADE قائم في D.\nنريد كتابة علاقة بين مربّعات أطوال أضلاعه الثلاثة ، مع تعليلها.\nأيّ تعليل ونتيجة صحيحان ؟",
 [("نظرية فيثاغورس: AD² = AE² + DE²","math.geo.hypotenuse-mal-choisie"),("عكس نظرية فيثاغورس: AE² = AD² + DE²","math.geo.pythagore-reciproque-role"),("نظرية فيثاغورس: AE² = AD² + DE²",None),("عكس نظرية فيثاغورس: AD² = AE² + DE²",None)],2,
 "المثلّث ADE قائم في D ، فوتره [AE] المقابل للزاوية القائمة ، والزاوية القائمة معلومة ، فنطبّق نظرية فيثاغورس المباشرة: AE² = AD² + DE² ✓. الخطأ الشائع: وضع مربّع [AD] وحده في طرف كأنّ [AD] هو الوتر ؛ أو استعمال عكس النظرية ، وهي تُثبت أنّ مثلّثًا قائم انطلاقًا من أطواله ، ولا تُستعمل حين تكون الزاوية القائمة معلومة.",1,"math.geo.pythagore",fig51_ade()))
q51.append(Q("المثلّث ADE قائم في D ، ونعلم أنّ الأطوال بالسنتمتر هي:\nAD = 2\nDE = 3\nما طول القطعة [AE] بالسنتمتر ؟",
 [("13","math.geo.pythagore-racine-oubliee"),("√5","math.geo.hypotenuse-mal-choisie"),("√10",None),("√13",None)],3,
 "المثلّث ADE قائم في D ، فوتره [AE] ، وبنظرية فيثاغورس AE² = AD² + DE² = 4 + 9 = 13 ، إذن AE = √13 cm ✓. الخطأ الشائع: التوقّف عند AE² = 13 ؛ أو عدّ [DE] وترًا فنجد AE² = 9 − 4 = 5 أي √5 ؛ أو مضاعفة الطولين بدل تربيعهما فنجد AE² = 2 × 2 + 3 × 2 = 10 أي √10.",1,"math.geo.pythagore",fig51_ade(('AD','DE'))))
q51.append(Q("المثلّث ADE قائم في D ، والنقطة B من نصف المستقيم [AE) ، والمستقيم العمودي على (AD) والمارّ من B يقطع (AD) في C.\nأيّ حجّة تثبت أنّ المستقيمين (DE) و (CB) متوازيان ؟",
 [("كلٌّ من (DE) و (CB) عمودي على المستقيم (AD)",None),("كلٌّ من (DE) و (CB) يقطع المستقيم (AD)",None),("كلٌّ من (DE) و (CB) يمرّ بنقطة من [AB]",None),("المستقيم (DE) عمودي على (AD) والمستقيم (CB) عمودي على (AB)",None)],0,
 "المثلّث ADE قائم في D ، فالمستقيم (DE) عمودي على (AD). والمستقيم (CB) عمودي على (AD) بالإنشاء. وكلّ مستقيمين عموديين على مستقيم واحد متوازيان ، إذن (DE) ∥ (CB) ✓ ، وهذا التوازي شرط تطبيق نظرية طاليس. الخطأ الشائع: الاكتفاء بأنّ المستقيمين يقطعان (AD) ، أو بأنّ كلًّا منهما يمرّ بنقطة من [AB] ، فهذا لا يعطي التوازي: لو نقلنا النقطة E على [AB] لبقي الأمران صحيحين ولما بقي (DE) موازيًا لـ (CB) ؛ أو ربط كلّ مستقيم بعمودي مختلف ، والقاعدة تشترط مستقيمًا واحدًا يعمدانه معًا ، و (CB) عمودي على (AD) لا على (AB).",2,"math.geo.droites-perp-para",fig51()))
q51.append(Q("في الشكل التالي ، (DE) ∥ (CB) ، والنقطة D من [AC] والنقطة E من [AB].\nأيّ سلسلة مساواة بين النسب صحيحة بنظرية طاليس ؟",
 [("AC/CD = AB/BE = CB/DE","math.geo.segment-mal-choisi"),("CD/AD = BE/AE = CB/DE","math.geo.thales-formes-melangees"),("AD/AC = AB/AE = CB/DE","math.geo.thales-rapport-inverse"),("AC/AD = AB/AE = CB/DE",None)],3,
 "(DE) ∥ (CB) والنقطتان D و E من [AC] و [AB] ، فبنظرية طاليس في المثلّث ACB: AD/AC = AE/AB = DE/CB ، أي بقلب النسب الثلاث معًا AC/AD = AB/AE = CB/DE ✓. الخطأ الشائع: قلب نسبة واحدة فقط ؛ أو أخذ القطعة الجزئيّة CD أو BE بدل القطعة الكاملة AC أو AB في النسبة ؛ أو مزج نسبة الجزء على الباقي (CD/AD) مع نسبة الكلّ على الجزء (CB/DE).",2,"math.geo.thales-direct",fig51()))
q51.append(Q("في الشكل التالي ، (DE) ∥ (CB) ، والنقطة D من [AC] والنقطة E من [AB] ، ونعلم أنّ الأطوال بالسنتمتر تحقّق:\nAD = 2\nAB = 3 × AE\nما طول القطعة [AC] بالسنتمتر ؟",
 [("2/3",'math.geo.thales-rapport-inverse'),("4","math.geo.segment-mal-choisi"),("5","math.num.operation-inverse-appliquee"),("6",None)],3,
 "(DE) ∥ (CB) ، فبنظرية طاليس AC/AD = AB/AE. وAB = 3 × AE ، فـ AB/AE = 3 ، إذن AC/2 = 3 ، ومنه AC = 2 × 3 = 6 cm ✓. الخطأ الشائع: قلب النسبة فنجد AC = 2 ÷ 3 = 2/3 ؛ أو إعطاء القطعة الجزئيّة CD بدل القطعة الكاملة [AC] ، وهي CD = AC − AD = 4 ؛ أو الجمع بدل الضرب في النسبة 3 فنجد 2 + 3 = 5.",3,"math.geo.thales-direct",fig51()))
q51.append(Q("نعتبر المثلّث ACB ، وقاعدته [CB] توازيها القطعة [DE] حيث D من [AC] و E من [AB].\nإذا كان طول [DE] ثلاثة سنتمترات ، وكان:\nAE = AB ÷ 3\nفما طول القاعدة [CB] بالسنتمتر ؟",
 [("1",'math.geo.thales-rapport-inverse'),("4,5","math.geo.segment-mal-choisi"),("6","math.geo.segment-mal-choisi"),("9",None)],3,
 "(DE) ∥ (CB) ، فبنظرية طاليس CB/DE = AB/AE = 3 ، ومنه CB = 3 × DE = 3 × 3 = 9 cm ✓. الخطأ الشائع: قلب النسبة فنجد CB = 3 ÷ 3 = 1 ؛ أو إعطاء القطعة الجزئيّة BE بدل القطعة الكاملة: BE/AE = 2 فنجد 6 ؛ أو استعمال النسبة AB/BE بدل AB/AE ، وهي تساوي 3/2 ، فنجد 3 × 3/2 = 4,5.",3,"math.geo.thales-direct",fig51()))
write("51-examen-2022-technique-ex3-triangle-droite-perpendiculaire-pythagore-parallelisme-thales.json",
 "🏛️ مناظرة 2022 (تقني) · التمرين 3 ⭐⭐: مثلّث وعمودي على ضلعه — فيثاغورس والتوازي وطاليس",2,"practice",75,15,51,q51)
