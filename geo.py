import math

def popu(p):
    inc=0.2
    for i in range(10):
        if i==5:
            inc=0.1
        p+=inc*p
    return p

p,cr,pop=input().split(' ')
p,cr,pop=float(p),float(cr),int(pop)
ms,n,xc,xs,xci,xcf,hc,tcell=0.25,3,0.15,0.3,0.2,1,1.35,2.9
Vsd=(pop*ms*365)/(p*cr*156)
Vscell=Vsd*tcell
Vs=Vscell*n
Acell=Vscell*15/13
Vccell=((tcell-1)*xc+xci)*Acell
Vcstack=Vccell*n
Vctop=Acell*(xcf-xci)
Vcside=2*(math.sqrt(Acell)*xci*hc*n)
Vc=Vcside+Vctop+Vcstack
Vr=(Vs+Vc)/Vs
pop=popu(pop)
V=(pop*ms*Vr*365)/(p*cr)
print(V)
