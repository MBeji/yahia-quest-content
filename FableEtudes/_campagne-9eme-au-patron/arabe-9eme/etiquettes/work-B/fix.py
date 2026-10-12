import sys
p,pairs=sys.argv[1],eval(open(sys.argv[2]).read())
s=open(p).read()
for a,b in pairs:
    assert a in s,a[:40]; s=s.replace(a,b)
open(p,'w').write(s)
