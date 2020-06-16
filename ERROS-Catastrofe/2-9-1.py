import matplotlib.pyplot as plt
import math
import numpy as np

x = 1 / 3 
y = list()

for i in range(0,100,1):
    x = 4*x - 1
    y.append(x)

xaxis = np.arange(len(y))
#plt.axis([len(cycle) - 40,len(cycle),-0.5,1.])

plt.axhline(xmin=0, xmax=1000, y=0.05 ,color='r', linestyle='-')

plt.plot(xaxis,y, color='blue', linewidth = 1.4)

plt.title('Exercício 2.9.1 - Livro colaborativo - Calculo Numérico com Python\n Com efeito catastrófico')
plt.xlabel('Número de Iterações', fontsize=16)
plt.ylabel('Valores da imagen', fontsize=16)
plt.show()

