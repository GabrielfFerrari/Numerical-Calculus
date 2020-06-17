import math as mt
import numpy as np
import matplotlib.pyplot as plt 

#Constants:

c  = 299792458 # in m/s
m  = 9.10938291 * pow(10,-31) # in kg
Em = pow(10,-9)

Ev = pow(10,-5)
dm = Em * m 

V = [0.1*c, 0.5*c, 0.99*c, 0.999*c] #Velocity arrays

for v in V:
    dv = Ev * v
    f = m*pow(c,2) * ( 1 /( pow((1 - pow(v/c,2)),1/2 )) - 1)

    dfv = (m*v) / ( pow( (1 - pow(v/c,2)), 3/2))
    dfm = pow(c,2) * ( 1 /( pow((1 - pow(v/c,2)),1/2 )) - 1)

    df = dfm * dm + dfv * dv
    Erf = df / f
    print('Valor da velocidade: {}\nValor da Função:{}\nErro Relativo: {}'.format(v,f,Erf))
    print(50*'-')
