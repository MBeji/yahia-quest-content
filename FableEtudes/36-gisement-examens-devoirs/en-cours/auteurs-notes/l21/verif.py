import math, itertools
from fractions import Fraction as F
r2=math.sqrt
def chk(name,key,wrongs):
    for w in wrongs: assert abs(key-w)>1e-9,(name,key,w)
    print("ok",name,round(key,4))
# 47
chk("47Q1",1500/10,[1500/100,1500,1500*10])
x=-1; chk("47Q2",(x-2)*x,[-3,-1,1])
AB,AC=8,6; BC=math.hypot(AB,AC); assert BC==10
chk("47Q3",BC,[AB+AC,BC**2,r2(AB**2-AC**2)])
chk("47Q4",AB+AC+math.pi*BC/2,[AB+AC+math.pi*BC,AB+AC+BC+math.pi*BC/2,AB+AC+BC+math.pi*BC])
assert abs((AB+AC+math.pi*5)-(14+5*math.pi))<1e-12
# 48
AB,AC=3,4;BC=5;AH=AB*AC/BC;chk("48Q4",AH,[BC/2,AB*BC/AC,12]);
assert abs(AH-2.4)<1e-12
HB=math.sqrt(AB**2-AH**2); chk("48Q5",HB,[AB-AH,AB**2-AH**2,math.sqrt(AB**2+AH**2)]); assert abs(HB-1.8)<1e-12
assert abs(AB**2/BC-1.8)<1e-12  # 2e chemin : AB^2=BH.BC
area=HB*AH/2; assert abs(area-2.16)<1e-12
chk("48Q6",area,[HB*AH,AB*AH/2,HB+AH])
real=area*(1000/100)**2; assert abs(real-216)<1e-9
# 2e chemin : cotes en m
assert abs((HB*10)*(AH*10)/2-216)<1e-9
chk("48Q7",real,[area*10,area*1000/10000,area*1000])
# 49
v=r2(2)*(r2(8)-r2(2)); chk("49Q1",v,[2*r2(3),4-r2(2),2*r2(2)]); assert abs(v-2)<1e-12
o=-(1-r2(3)); chk("49Q2",o,[-1-r2(3),1+r2(3),1/(1-r2(3))]); assert abs(o-(r2(3)-1))<1e-12
a=abs(1-r2(2))-r2(2); chk("49Q3",a,[1,1-2*r2(2),2*r2(2)-1]); assert abs(a+1)<1e-12
ac=math.sqrt(50**2-40**2); chk("49Q4",ac,[10,900,r2(4100)]); assert abs(ac-30)<1e-9
# 50
AS=math.hypot(2.5,6); assert abs(AS-6.5)<1e-12; chk("50Q2",AS,[8.5,42.25,r2(29.75)])
SN=6-1.8; chk("50Q5",SN,[1.8,7.8,10.8]); assert abs(SN-4.2)<1e-12
MN=SN/6*2.5; chk("50Q6",MN,[1.8/6*2.5,1.75+0*1,SN*2.5,2.5*6/SN]) if False else None
assert abs(MN-1.75)<1e-12
for w in [1.8/6*2.5, SN*2.5, 2.5*6/SN]: assert abs(w-MN)>1e-9
assert abs(MN/2.5-SN/6)<1e-12
# 2e chemin : Thales avec SM/SA : SM=SA-AM
SM=AS-1.95; chk("50Q7",SM,[1.95,6-1.95,AS+1.95]); assert abs(SM-4.55)<1e-12
assert abs(SM/AS-SN/6)<1e-12  # coherence SM/SA=SN/SB=0.7
# 51
AE=math.hypot(2,3); chk("51Q2",AE,[13,r2(5),r2(10)]); assert abs(AE**2-13)<1e-12
AC=2*3; chk("51Q5",AC,[2/3,AC-2,5]); CB=3*3; chk("51Q6",CB,[1,4.5,2*3])
# coherence geometrique (coordonnees) : C(0,0) A(6,0) D(4,0) B(0,9) E(4,3)
A=(6,0);D=(4,0);B=(0,9);E=(4,3)
d=lambda p,q: math.dist(p,q)
assert abs(d(A,D)-2)<1e-12 and abs(d(D,E)-3)<1e-12 and abs(d(A,B)-3*d(A,E))<1e-12 and abs(d(A,(0,0))-6)<1e-12 and abs(d((0,0),B)-9)<1e-12
print("ALL OK")
# tour de corrections
chk("47Q3b",10,[r2(14),28,2*r2(7)]); chk("48Q2b",5,[r2(7),r2(12),49])
chk("48Q4b",12/5,[2.5,12/7,12/25]); chk("48Q5b",1.8,[0.6,5.4,r2(14.76)])
SA,SM,SN,SB,MN,AB_,MA=6.5,4.55,4.2,6,1.75,2.5,1.95
key=(SM/SA,SN/SB,MN/AB_); assert max(key)-min(key)<1e-12
for o in [(SA/SM,SB/SN,MN/AB_),(SM/MA,SB/SN,AB_/MN),(SA/SM,SN/(6-SN),AB_/MN)]: assert max(o)-min(o)>1e-6
print("TOUR OK")
