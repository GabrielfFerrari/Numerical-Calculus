

V  = 220 
Vo = 220
a  = 0.8



Vi =   V*(1.01)
Vio = Vo*(1.03)
ai =   a*(1.04)
I = pow((Vi /Vio), ai)
print('Máximo: {}'.format(I))
Vm =  V*(1-0.01)
Vn = Vo*(1-0.03)
am =  a*(1-0.04)
In = pow( (Vm /Vn), am )
print('Mínimo: {}'.format(In))
Ir = pow((V /Vo), a)
print('Medio :{}'.format(Ir))


Variation = I - In
err = Variation / Ir
print(err)
