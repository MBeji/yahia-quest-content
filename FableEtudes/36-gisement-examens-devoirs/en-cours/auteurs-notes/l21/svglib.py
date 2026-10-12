import math
INK="#0f172a"; GREY="#64748b"; GREEN="#0f6e56"
def f(x):
    s=("%.1f"%x).rstrip('0').rstrip('.')
    return s
def svg(w,h,title,body):
    return '<svg viewBox="0 0 %d %d"><title>%s</title>%s</svg>'%(w,h,title,body)
def poly(pts,fill=True,dash=False,color=INK,sw=2.2,op=0.04):
    p=" ".join("%s,%s"%(f(x),f(y)) for x,y in pts)
    s=""
    if fill: s+='<polygon points="%s" fill="%s" fill-opacity="%s"/>'%(p,INK,op)
    s+='<polygon points="%s" fill="none" stroke="%s" stroke-width="%s" stroke-linejoin="round"/>'%(p,color,sw)
    return s
def seg(a,b,color=INK,sw=2.2,dash=False):
    d=' stroke-dasharray="6 5"' if dash else ''
    return '<path d="M%s %s L%s %s" fill="none" stroke="%s" stroke-width="%s" stroke-linecap="round"%s/>'%(f(a[0]),f(a[1]),f(b[0]),f(b[1]),color,sw,d)
def rightangle(v,p,q,s=11):
    # right angle mark at v between directions to p and q
    def u(a):
        dx,dy=a[0]-v[0],a[1]-v[1]; n=math.hypot(dx,dy); return dx/n,dy/n
    ux,uy=u(p); wx,wy=u(q)
    a=(v[0]+ux*s,v[1]+uy*s); c=(v[0]+wx*s,v[1]+wy*s); b=(a[0]+wx*s,a[1]+wy*s)
    return '<path d="M%s %s L%s %s L%s %s" fill="none" stroke="%s" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>'%(f(a[0]),f(a[1]),f(b[0]),f(b[1]),f(c[0]),f(c[1]),INK)
def dots(pts):
    return '<g fill="%s">'%INK+"".join('<circle cx="%s" cy="%s" r="3.8"/>'%(f(x),f(y)) for x,y in pts)+'</g>'
def labels(items,size=15,color=INK):
    s='<g font-size="%d" font-weight="700" direction="ltr" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">'%size
    for (t,x,y) in items:
        s+='<text x="%s" y="%s" text-anchor="middle" fill="%s">%s</text>'%(f(x),f(y),color,t)
    return s+'</g>'
def dim(items):
    return labels(items,13,GREY)
