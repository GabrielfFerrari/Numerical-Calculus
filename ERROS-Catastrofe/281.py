import math
x  = 2
y  = 10
dy = 1
dx = 0.02

dtf = ( (4*pow(y,3)) / (pow((1+pow(y,4)),2)) ) *pow(math.e,x)*dy + ( (pow(math.e,x)*pow(y,4)) / (1+pow(y,4)) )*dx



f = ((pow(y,4) *pow(math.e,2)) / (1+pow(y,4)))

rz2 = dtf / f

print(dtf)
print(rz2)
