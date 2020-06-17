import math

a = [0.1, 0.01, 0.001]
for x in a: 
    f = pow(math.e,1/x) / (1 + pow(math.e,1/x))
    print(f)


print('-------------------------------------')
#for y in a:
#    f = 1 / (1 + pow(math.e,-1/y))
#    print(f)
