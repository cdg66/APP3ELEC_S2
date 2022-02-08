

import numpy as np
import matplotlib.pyplot as plt
a = np.genfromtxt('muon.txt', skip_header=2, delimiter=',', dtype=float)
ax = a[:,0:2]
plt.plot(ax)
plt.show()
#plt.legend()
print(ax)

















