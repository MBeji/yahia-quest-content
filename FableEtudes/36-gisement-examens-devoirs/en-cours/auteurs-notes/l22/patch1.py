import re
W='/tmp/claude-0/-home-user/b03814da-e5f9-5a74-bf03-e7c23b20207a/scratchpad/l22-work/'
src=open(W+'gen.py',encoding='utf-8').read()
parts=re.split(r'(?=^q\d\d\.append\()|(?=^d\d\d = hdr)|(?=^# =====)',src,flags=re.M)
idx={'q18':[],'q07':[],'q12':[]}
for i,p in enumerate(parts):
    m=re.match(r'(q\d\d)\.append\(',p)
    if m: idx[m.group(1)].append(i)
def rep(k,n,new): parts[idx[k][n]]=new.strip('\n')+'\n'

rep('q18',5,'''
q18.append(Q('ABC مثلّث متقايس الضلعين قمّته A، وO منتصف [BC]، والنقطة E من [AB] والنقطة F من [AC] حيث (EF) // (BC)، ونسمّي K نقطة تقاطع (AO) و(EF). الأطوال بالصنتمتر :\\nAB = 50\\nAO = 40\\nAE = 15\\nما طول [AK] بالصنتمتر ؟\\n' + svg_tri('المثلّث ABC والنقاط E وF وK وO', show_o=True, show_ef=True, show_k=True),
    ['12', '5', '15', '400/3'], 0,
    'K على [AO] وE على [AB] والمستقيمان (KE) و(OB) متوازيان، فبطاليس في المثلّث ABO: AK/AO = AE/AB = 15/50 = 3/10، إذن AK = 40 × 3/10 = 12 cm ✓.\\nالخطأ الشائع: حساب الفرق 40 − (50 − 15) = 5 بدل النسبة؛ أو قلب النسبة فنجد 40 × 50 ÷ 15 = 400/3؛ أو أخذ AK = AE = 15.',
    2, ['math.geo.thales-direct'], {'5': T_ + 'thales-longueurs-au-lieu-de-rapports', '400/3': T_ + 'thales-rapport-inverse'}))
''')
rep('q18',6,'''
q18.append(Q('ABC مثلّث متقايس الضلعين قمّته A، وO منتصف [BC] و(AO) عمودي على (BC)، والنقطة E من [AB] والنقطة F من [AC] حيث (EF) // (BC)، ونسمّي K نقطة تقاطع (AO) و(EF). الأطوال بالصنتمتر :\\nBC = 60\\nAO = 40\\nEF = 18\\nAK = 12\\nنحصل على شبه المنحرف EFCB بقصّ المثلّث AEF من المثلّث ABC.\\nما مساحة شبه المنحرف EFCB بالصنتمتر المربّع ؟\\n' + svg_tri('المثلّث ABC وشبه المنحرف EFCB', show_o=True, show_ef=True, show_k=True, right=True),
    ['1200', '984', '1092', '840'], 2,
    'نحصل على مساحة شبه المنحرف EFCB بطرح مساحة المثلّث AEF من مساحة المثلّث ABC. ارتفاع ABC هو AO لأنّ (AO) عمودي على (BC)، وارتفاع AEF هو AK لأنّ (EF) // (BC) فالمستقيم (AK) عمودي على (EF). مساحة ABC = 60 × 40 ÷ 2 = 1200 ومساحة AEF = 18 × 12 ÷ 2 = 108، إذن مساحة EFCB = 1200 − 108 = 1092 cm² ✓.\\nالخطأ الشائع: الاكتفاء بمساحة المثلّث ABC أي 1200 دون طرح AEF؛ أو نسيان القسمة على 2 في مساحة AEF فنجد 1200 − 216 = 984؛ أو أخذ AO ارتفاعًا للمثلّث AEF فنجد 1200 − 360 = 840.',
    2, ['math.mes.aires'], {'1200': 'math.alg.reponse-a-l-autre-inconnue', '984': 'math.mes.aire-triangle-sans-moitie'}))
''')
# Q8: modify only options/explanation/tags
b=parts[idx['q18'][7]]
b=b.replace("['12', '15', '50', '28'], 3,","['12', '15', '35', '28'], 3,")
b=re.sub(r"'الخطأ الشائع: اعتماد القطعة \[AK\][^']*'","'الخطأ الشائع: اعتماد القطعة [AK] وطولها 12، وهي الجزء الأعلى من [AO] لا المسافة بين القاعدتين؛ أو أخذ AE = 15 أو الساق المائلة [EB] = 50 − 15 = 35 ارتفاعًا، والارتفاع عمودي على القاعدتين.'",b) if False else b
parts[idx['q18'][7]]=b
open(W+'gen.py','w',encoding='utf-8').write(''.join(parts))
