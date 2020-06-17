import matplotlib.pyplot as plt
import math
import numpy as np

x = 1 / 3 
y = list()

for i in range(0,1000,1):
    x = 4*x - 1
    y.append(x)

xaxis = np.arange(len(y))


print(y)

plt.plot(xaxis,y, 'b--', linewidth = 1.4)

plt.title('Exercício 2.9.1 - Livro colaborativo - Calculo Numérico com Python\n Com efeito catastrófico')
plt.xlabel('Número de Iterações (1000 passos)', fontsize=16)
plt.ylabel('Valor iterado', fontsize=16)
plt.savefig('291-exec.png', format='png')     
plt.show()
