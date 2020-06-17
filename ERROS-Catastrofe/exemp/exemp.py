import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = [2, 1, 76, 140, 286, 267, 60, 271, 5, 13, 9, 76, 77, 6, 2, 27, 22, 1, 12, 7, 
     19, 81, 11, 173, 13, 7, 16, 19, 23, 197, 167, 1]
x = pd.Series(x)

# histogram on linear scale
plt.subplot(211)
hist, bins, _ = plt.hist(x, bins=8) # Plot
print(bins)
# histogram on log scale. 
# Use non-equal bin sizes, such that they look equal on log scale.
#np.logspace(np.log10(), stop, num=num, endpoint=endpoint)

logbins = np.logspace(np.log10(bins[0]),np.log10(bins[-1]),len(bins))
plt.subplot(212)
plt.hist(x, bins=logbins)
plt.xscale('log')
plt.show()

