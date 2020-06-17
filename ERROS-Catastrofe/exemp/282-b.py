import math as mt
V  = 220 
Vo = 220
a  = 0.8

dV =  (a * pow(V,a-1) / (pow(Vo, a)))*2.2 
dVo = (-a*pow(V/Vo,a)/Vo)*6.6 
da =  (pow(V/Vo,6)* mt.log((V/Vo)) )* 0.32
if dV < 0:
    dV= dV*(-1)
if dVo < 0:
    dVo= dVo*(-1)
if da < 0:
    da= da*(-1)
dI = dV + dVo + da
I = pow(V/Vo, a)

print(dI/I)











