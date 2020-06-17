import matplotlib.pyplot as plt
import numpy as np

f = list()
axisx=list()
for x in range(0, 17,1):
    f.append(((1+5*pow(10,-x)) - 1) / (5*pow(10,-x)))
    axisx.append(pow(10,-x))

#axisx = np.arange(len(f))

#plt.ylim(0,2)
#plt.xlim(0,2)
plt.title('Exercício 2.9.1 \n com efeito Catástrofe')
plt.plot(sorted(axisx,reverse=True), sorted(f,reverse=True), 'b-')
plt.savefig('2-9-2.png',format='png')
plt.xscale(u"log")
plt.show()
