

import numpy as np
import matplotlib.pyplot as plt
a = np.genfromtxt('S2GE_APP3_Problematique_Detecteur_Primaire.csv', delimiter=',', dtype=float)
ax = a[:,0:2]
plt.plot(ax)
plt.show()
#plt.legend()
print(ax)

















