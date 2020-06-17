import matplotlib.pyplot as plt
import numpy as np

x=np.array([1,2,3,4,5])
def f(x):
    return 10**(x-1)

plt.plot(x,f(x))
plt.xscale(u"log")

plt.show()
