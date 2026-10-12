import math, random
INK="#0f172a"
def f(x): 
    return ("%.1f"%x).rstrip('0').rstrip('.')
def svg(w,h,title,body):
    return f'<svg viewBox="0 0 {w} {h}"><title>{title}</title><rect x="0" y="0" width="{w}" height="{h}" fill="#ffffff"/>{body}</svg>'
def g(x,y,s,body):
    return f'<g transform="translate({f(x)},{f(y)}) scale({s})">{body}</g>'
def text(x,y,t,size=12,anchor="middle",fill=INK,weight=700):
    return (f'<text x="{f(x)}" y="{f(y)}" text-anchor="{anchor}" font-size="{size}" font-weight="{weight}" fill="{fill}" '
            f'paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">{t}</text>')
def arrow(x1,y1,x2,y2):
    # line from (x1,y1) to tip (x2,y2) with head
    a=math.atan2(y2-y1,x2-x1); L=6
    bx=x2-L*math.cos(a); by=y2-L*math.sin(a)
    px=-math.sin(a)*2.6; py=math.cos(a)*2.6
    return (f'<line x1="{f(x1)}" y1="{f(y1)}" x2="{f(bx)}" y2="{f(by)}" stroke="{INK}" stroke-width="1.4"/>'
            f'<polygon points="{f(x2)},{f(y2)} {f(bx+px)},{f(by+py)} {f(bx-px)},{f(by-py)}" fill="{INK}"/>')
def circ(x,y,r,fill="none",stroke=INK,sw=1.4):
    return f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r)}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
def ell(x,y,rx,ry,fill="none",stroke=INK,sw=1.4,rot=0):
    t=f' transform="rotate({rot} {f(x)} {f(y)})"' if rot else ''
    return f'<ellipse cx="{f(x)}" cy="{f(y)}" rx="{f(rx)}" ry="{f(ry)}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{t}/>'

# ---- local drawings (origin = centre) ----
def sperm():
    # head centre (0,-34); mid piece y -22..-4 ; tail loop
    b=''
    b+=ell(0,-34,8.5,12,fill="#374151",stroke=INK,sw=1.5)
    for (x,y) in [(-3,-38),(2,-31),(-2,-27),(3,-39),(0,-34)]:
        b+=f'<circle cx="{x}" cy="{y}" r="1.1" fill="#9ca3af"/>'
    b+='<path d="M-7.5,-39 C-5,-50 5,-50 7.5,-39 C4,-43 -4,-43 -7.5,-39 Z" fill="#dc2626" stroke="#7f1d1d" stroke-width="1"/>'
    for i in range(6):
        y=-21+i*3.6
        b+=f'<rect x="-4.6" y="{f(y)}" width="9.2" height="2.8" rx="1.2" fill="#ffffff" stroke="{INK}" stroke-width="1"/>'
    b+=f'<path d="M0,-3 C0,26 -2,40 8,46 C20,52 28,40 22,30 C18,22 6,26 8,36" fill="none" stroke="{INK}" stroke-width="1.5" stroke-linecap="round"/>'
    return b
def corona(r=43,n=22,size=3.4):
    b=''
    for i in range(n):
        a=2*math.pi*i/n
        x=r*math.cos(a); y=r*math.sin(a)
        b+=ell(x,y,size,size*1.15,fill="#3b82f6",stroke="#1e3a8a",sw=1,rot=int(math.degrees(a)+90))
    return b
def ovule(nucleus="single",polar=1,crown=True):
    b=''
    if crown: b+=corona()
    b+=circ(0,0,38,fill="#e2e8f0",stroke=INK,sw=2)
    b+=circ(0,0,35,fill="none",stroke=INK,sw=1)
    b+=circ(0,0,28,fill="#fbcfe8",stroke="#be185d",sw=1.5)
    for i in range(14):
        a=2*math.pi*i/14
        b+=f'<circle cx="{f(23*math.cos(a))}" cy="{f(23*math.sin(a))}" r="1.3" fill="#dc2626"/>'
    if nucleus=="single":
        b+=circ(-2,-8,6.5,fill="#1d4ed8",stroke="#1e3a8a",sw=1)
    elif nucleus=="zygote":
        b+=circ(0,2,7.5,fill="#312e81",stroke=INK,sw=1)
    elif nucleus=="two":
        b+=circ(-5,2,6.5,fill="#312e81",stroke=INK,sw=1)+circ(6,3,6,fill="#312e81",stroke=INK,sw=1)
    if polar==1:
        b+=ell(7,-31.5,5.2,3,fill="#b45309",stroke="#7c2d12",sw=1)
    elif polar==2:
        b+=ell(-3,-31.5,4.6,2.8,fill="#b45309",stroke="#7c2d12",sw=1)+ell(8,-31,4.2,2.7,fill="#b45309",stroke="#7c2d12",sw=1)
    return b
def morula():
    b=circ(0,0,34,fill="#cbd5e1",stroke="#475569",sw=2)
    b+=circ(0,0,28,fill="#ffffff",stroke="#475569",sw=1)
    pts=[]
    d=9.0
    for row in range(-3,4):
        for col in range(-3,4):
            x=col*d+(d/2 if row%2 else 0); y=row*d*0.87
            if math.hypot(x,y)<=22.5: pts.append((x,y))
    for (x,y) in pts:
        b+=circ(x,y,4.2,fill="#fde68a",stroke=INK,sw=1)
    return b
def free_ovule_burst():
    b=''
    b+=f'<path d="M-30,6 C-34,40 34,40 30,6" fill="#fde2e4" stroke="{INK}" stroke-width="1.8"/>'
    b+=f'<path d="M-24,12 C-26,34 26,34 24,12" fill="none" stroke="{INK}" stroke-width="1.2" stroke-dasharray="1.5 2.5"/>'
    b+=f'<path d="M-30,6 L-36,2 M30,6 L36,2" stroke="{INK}" stroke-width="1.8" stroke-linecap="round"/>'
    # ovule leaving, up
    for i in range(12):
        a=2*math.pi*i/12
        b+=f'<line x1="{f(8+10*math.cos(a))}" y1="{f(-20+10*math.sin(a))}" x2="{f(8+15*math.cos(a))}" y2="{f(-20+15*math.sin(a))}" stroke="{INK}" stroke-width="1"/>'
    b+=circ(8,-20,10,fill="#374151",stroke=INK,sw=1.5)+circ(8,-20,4,fill="#ffffff",stroke=INK,sw=1)
    return b
def blastocyst_in_wall():
    b=''
    b+=f'<path d="M-40,42 L-40,10 Q-32,6 -26,10 Q-20,18 -9,20 Q0,22 9,20 Q20,18 26,10 Q32,6 40,10 L40,42 Z" fill="#f9a8d4" stroke="{INK}" stroke-width="1.5"/>'
    for (x,y) in [(-30,24),(-20,32),(-8,30),(4,34),(14,28),(26,34),(34,22),(-34,36),(20,38),(-14,38)]:
        b+=f'<circle cx="{x}" cy="{y}" r="1.4" fill="{INK}"/>'
    for x in (-34,-28,28,34):
        b+=ell(x,8,2,3.4,fill="#fbbf24",stroke=INK,sw=0.8)
    b+=circ(0,-4,22,fill="#fef3c7",stroke=INK,sw=1.6)
    for (x,y) in [(-7,10),(0,11),(7,10),(-4,5),(4,5),(0,0)]:
        b+=circ(x,y,3.2,fill="#f59e0b",stroke=INK,sw=0.9)
    return b
# ---- charts ----
def wig(d,per,amp,ph=0): return amp*math.sin(2*math.pi*d/per+ph)
def temp(d,woman):
    low=lambda d:36.6+wig(d,4.7,0.07)+wig(d,2.1,0.03)
    high=lambda d:37.2+wig(d,5.3,0.06)+wig(d,2.3,0.03)
    def mix(a,b,t): return a+(b-a)*t
    ramp=lambda d,d0,w: min(1,max(0,(d-d0)/w))
    # events: rise at 13, drop at 30, rise at 41, drop at 61, rise at 69
    if d<2: return mix(36.9,low(d),d/2)
    if d<12.6: return low(d)
    if d<14.4: return mix(low(d),high(d),ramp(d,12.6,1.8))
    if d<29.5: return high(d)
    if d<31.5: return mix(high(d),low(d),ramp(d,29.5,2))
    if d<40.5: return low(d)
    if d<42.3: return mix(low(d),high(d),ramp(d,40.5,1.8))
    if woman=='B': return high(d)
    if d<60: return high(d)
    if d<62: return mix(high(d),low(d),ramp(d,60,2))
    if d<68.5: return low(d)
    if d<70.3: return mix(low(d),high(d),ramp(d,68.5,1.8))
    return high(d)
def chart(woman,ox=0,oy=0):
    X=lambda d:32+2.2*d
    Y=lambda t:78-(t-36.5)*56
    b=''
    b+=f'<rect x="{ox+1}" y="{oy+1}" width="230" height="116" fill="none" stroke="#94a3b8" stroke-width="1"/>'
    b+=f'<line x1="{ox+30}" y1="{oy+98}" x2="{ox+226}" y2="{oy+98}" stroke="{INK}" stroke-width="1.4"/>'
    b+=f'<polygon points="{ox+229},{oy+98} {ox+222},{oy+95} {ox+222},{oy+101}" fill="{INK}"/>'
    b+=f'<line x1="{ox+30}" y1="{oy+98}" x2="{ox+30}" y2="{oy+8}" stroke="{INK}" stroke-width="1.4"/>'
    b+=f'<polygon points="{ox+30},{oy+5} {ox+27},{oy+12} {ox+33},{oy+12}" fill="{INK}"/>'
    for t,lab in ((36.5,'36,5'),(37.0,'37,0'),(37.5,'37,5')):
        b+=f'<line x1="{ox+27}" y1="{oy+Y(t):.1f}" x2="{ox+33}" y2="{oy+Y(t):.1f}" stroke="{INK}" stroke-width="1.2"/>'
        b+=text(ox+25,oy+Y(t)+3.5,lab,9,'end',weight=500)
    b+=text(ox+38,oy+10,'°C',9,'start',weight=500)
    for d,lab in ((0,'1/4'),(13,'14/4'),(30,'1/5'),(41,'12/5'),(61,'1/6'),(69,'9/6')):
        x=ox+X(d)
        b+=f'<line x1="{x:.1f}" y1="{oy+98}" x2="{x:.1f}" y2="{oy+102}" stroke="{INK}" stroke-width="1.2"/>'
        if d: b+=f'<line x1="{x:.1f}" y1="{oy+14}" x2="{x:.1f}" y2="{oy+98}" stroke="#94a3b8" stroke-width="0.9" stroke-dasharray="3 3"/>'
        b+=text(x,oy+112,lab,8.5,'middle',weight=500)
    pts=' '.join(f'{ox+X(d/2):.1f},{oy+Y(temp(d/2,woman)):.1f}' for d in range(0,171))
    b+=f'<polyline points="{pts}" fill="none" stroke="#b91c1c" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round"/>'
    return b
