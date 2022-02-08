

import numpy as np
import matplotlib.pyplot as plt

def axis(array, colum):
    ret = np.array([])
    for i in range(len(array)):
        ret = np.append(ret, array[i][colum])
    return ret
# reteving data
a = np.genfromtxt('S2GE_APP3_Problematique_Detecteur_Primaire.csv', delimiter=',', dtype=float)
# isolate axis
index = axis(a, 0)
temps = axis(a, 1)
tension = axis(a, 2)
tempsmortcumul = axis(a, 3)
temeperatue = axis(a, 4)

# data processing


# ploting

plt.plot(temps[0:10], temeperatue[0:10], ".")
plt.show()
#plt.legend()
print()
















