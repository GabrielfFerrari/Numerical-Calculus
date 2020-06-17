import math

x = 100
f = 1 / ( pow(pow(math.e,2*x)+1,1/2) + pow(math.e,x))
print('Primeira expressão: {}'.format(f))


f1 = x**2 / ( pow(pow( math.e,2*x) + x**2,1/2) + pow(math.e,x))
print('Segunda expressão: {}'.format(f1))
