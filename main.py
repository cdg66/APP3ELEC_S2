

import numpy as np
import matplotlib.pyplot as plt

def axis(array, colum):
    ret = np.array([])
    for i in range(len(array)):
        ret = np.append(ret, array[i][colum])
    return ret


def histogramme(x, width, plt):
    histmin = np.floor(min(x))
    histmax = np.ceil(max(x)) + width
    bins = np.arange(histmin, histmax, width)
    plt.hist(x, bins=bins)
#    plt.show()

# reteving data
a = np.genfromtxt('S2GE_APP3_Problematique_Detecteur_Primaire.csv', delimiter=',', dtype=float)
# isolate axis
index = axis(a, 0)
temps = axis(a, 1)
tension = axis(a, 2)
tempsmortcumul = axis(a, 3)
temeperatue = axis(a, 4)

# data processing

histogramme(tension, 100, plt)

#ploting
plt.show()
















