

import numpy as np
import matplotlib.pyplot as plt

def axis(array, colum):
    ret = np.array([])
    for i in range(len(array)):
        ret = np.append(ret, array[i][colum])
    return ret

a = np.genfromtxt('S2GE_APP3_Problematique_Detecteur_Primaire.csv', delimiter=',', dtype=float)
#ax = a[:,0:2] #test
#plt.plot(ax)  #test #todo remove
index = axis(a, 0)
temps = axis(a, 1)
tension = axis(a, 2)
tempsmortcumul = axis(a, 3)
temeperatue = axis(a, 4)
plt.plot(temps, temeperatue)
plt.show()
#plt.legend()
print(ax)
















