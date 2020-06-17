import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 
import math

y = list()
t = list()

for k in range(0,20,1):
    y.append( (1 + 1/pow(10,k) )**pow(10,k) )
    t.append(pow(10,k))

xn = np.arange(len(y))
xp = pd.Series(y)

print(xp)

plt.title('Sequência do limite fundamental de euller \n Com efeito catástrofe')
plt.ylim([0,4])
l = np.logspace(0, 20, 20, endpoint=True, base=10)


plt.xscale(u"log")



plt.plot(t,y)
plt.savefig('293.png',format='png')


plt.show()
