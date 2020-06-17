import math

i = [-5,-6,-7,-8,-9,-200]
for x in i:
    f1 = (1 - math.cos(pow(10,x))) / (pow(x,2))
    print('função f1: {}'.format(f1))
    f2 = 1/2 * ( math.sin(pow(10,x)/2) /(pow(10,x)/2))
    print('função f2: {}'.format(f2))
    if x < -5:
        fesp = 1/2 - pow(10,x)/24
        print('Arredondamento especial: {}'.format(fesp))
    print('-------------------------')
