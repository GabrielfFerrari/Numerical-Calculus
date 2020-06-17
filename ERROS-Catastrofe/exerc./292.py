import math

#questão 292
items = ['a','b','c','d']
x = pow(10,-17)

for choose in items:
    print('Item: {}'.format(choose) )

value = str(input('Escolha o valor para visualizar: '))

if value == 'a':
    f1 = (1 - math.cos(x)) /pow(x,2)
    print(f1)
    f = (math.sin(x))**2 / (pow(x,2)*(1+math.cos(x)))
    print(f)

if value == 'b':
    f1 = pow(1+x,1/2) - 1
    print(f1)
    f = x / (pow(1+x,1/2) + 1)
    print(f)
if value == 'c':
    f1 = pow( x + pow(10,6),1/2) - pow(10,3)
    print(f1)
    f =  x   / ( pow(x + pow(10,6),1/2) + pow(10,3))
    print(f)                    
if value == 'd':
    f1 = pow( pow(math.e,x) + 1, 1/2) - pow(2,1/2)
    print(f1)
    f = ( pow(math.e,1/2) - 1) / (pow(math.e + 1,x) + pow(2,1/2) )
    print(f)                 
    y = pow(math.e,x) -1
    f2 = (y) / (pow(y+2,1/2) + pow(2,1/2) )
    print(f2)                    

