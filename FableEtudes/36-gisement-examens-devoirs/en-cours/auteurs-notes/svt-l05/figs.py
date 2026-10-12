from svglib import *
def fig_q1():
    b=g(200,56,0.95,sperm())+g(120,55,0.82,ovule("single",1,True))+g(40,55,0.95,morula())
    return svg(240,112,"ثلاثة رسوم لبنى مجهريّة مرتّبة من اليمين إلى اليسار: خليّة مستطيلة ذات رأس وذيل طويل، ثمّ خليّة كرويّة كبيرة محاطة بغلاف وبتاج من خلايا صغيرة، ثمّ كتلة كرويّة من خلايا كثيرة متراصّة داخل غلاف سميك",b)
def fig_q2():
    b=g(64,62,1,ovule("single",1,True))+g(186,60,1,sperm())
    b+=arrow(24,22,67,62-31.5)
    b+=text(14,20,'2',14)
    import math
    for i in (8,9):
        a=2*math.pi*i/22
        b+=arrow(26,106,64+46.5*math.cos(a),62+46.5*math.sin(a))
    b+=text(14,114,'3',14)
    b+=arrow(138,58,181,57)+text(130,62,'1',14)
    b+=arrow(222,14,194,17)+text(224,26,'4',14)
    return svg(232,124,"رسمان لبنيتين: على اليمين خليّة ذات رأس وقطعة وسطى وذيل طويل، وعلى اليسار خليّة كرويّة كبيرة محاطة بغلاف وبخلايا صغيرة؛ الرقم 1 يشير إلى الجزء الملتفّ خلف الرأس، والرقم 2 إلى جسم صغير بين الخليّة والغلاف، والرقم 3 إلى خليّتين من الخلايا المحيطة بالغلاف، والرقم 4 إلى القلنسوة الحمراء فوق الرأس",b)
def cx_p(x): return x
def fig_09(only=None):
    panels=[(200,'1',lambda:free_ovule_burst()),(120,'2',lambda:ovule("two",2,True)),(40,'3',lambda:blastocyst_in_wall())]
    b=''
    for (x,n,fn) in panels:
        if only and n not in only: continue
        sc=0.82 if n=='2' else 0.95
        b+=g(x,52,sc,fn())+text(x,106,n,14)
    b+='<line x1="80" y1="6" x2="80" y2="100" stroke="#cbd5e1" stroke-width="1"/><line x1="160" y1="6" x2="160" y2="100" stroke="#cbd5e1" stroke-width="1"/>'
    return svg(240,114,"ثلاثة رسوم مرقّمة من 1 إلى 3 من اليمين إلى اليسار: الرسم 1 جريب مفتوح الجدار تخرج منه خليّة كرويّة محاطة بخيوط، والرسم 2 خليّة كبيرة محاطة بغلاف وبخلايا صغيرة وفي وسطها كتلتان داكنتان متجاورتان مع جسمين صغيرين قرب الغلاف، والرسم 3 كيس صغير مجوّف ذو كتلة خلايا في قطبه السفلي منغرس في سطح غشاء مخاطيّ غير منتظم",b)
def fig_09_p2():
    b=g(60,56,1.0,ovule("two",2,True))
    return svg(120,112,"رسم لخليّة كبيرة محاطة بغلاف وبخلايا صغيرة، وفي وسطها كتلتان داكنتان متجاورتان وقرب الغلاف جسمان صغيران",b)
def fig_chart(w):
    return svg(232,118,"منحنى تغيّر درجة حرارة الجسم بالدرجة المئوية خلال ثلاثة أشهر لامرأة، التواريخ على المحور الأفقي مكتوبة بصيغة اليوم/الشهر" ,chart(w))
def fig_chart2():
    b=chart('A')+chart('B',0,0)
    return None
def fig_doc5():
    b=g(70,58,1.1,ovule("zygote",2,True))
    return svg(140,116,"رسم لخليّة كرويّة ذات نواة واحدة وسطها، محاطة بغلاف وبخلايا صغيرة، وقرب الغلاف في الأعلى جسمان صغيران",b)
if __name__=="__main__":
    import sys
    out='/tmp/claude-0/-home-user/b03814da-e5f9-5a74-bf03-e7c23b20207a/scratchpad/svt-l05-work/prev'
    import os; os.makedirs(out,exist_ok=True)
    for n,s in [('q1',fig_q1()),('q2',fig_q2()),('f09',fig_09()),('cA',fig_chart('A')),('cB',fig_chart('B')),('d5',fig_doc5())]:
        open(f'{out}/{n}.svg','w').write(s)
    html='<html><body style="background:#fff">'+''.join(f'<div style="width:232px;margin:8px;display:inline-block">{open(f"{out}/{n}.svg").read()}</div>' for n in ['q1','q2','f09','cA','cB','d5'])+'</body></html>'
    open(out+'/prev.html','w').write(html)
