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
    plt.show()


def coincidance(T1, T2, DT):
    TR = np.zeros(len(T1))
    dernierecoincidence = 0
    for i in range(0, len(T1)):

        for j in range(dernierecoincidence, len(T1)):

            delta = T1[i] - T2[j]
            if delta < 0:  # depasse
                # save 0
                TR[i] = 0
                break
            if delta <= DT:  # C
                dernierecoincidence = j
                # save 1
                TR[i] = 1
                break
            if delta >= DT:  # NC
                pass

    return TR

def main():
    # reteving datas
    prim = np.genfromtxt('S2GE_APP3_Problematique_Detecteur_Primaire.csv', delimiter=',', dtype=float)
    sec = np.genfromtxt('S2GE_APP3_Problematique_Detecteur_Secondaire.csv', delimiter=',', dtype=float)
    # isolate axis
    # index
    index = axis(prim, 0)
    # tension
    prim_tension = axis(prim, 2)
    sec_tension = axis(sec, 2)
    # temps
    temps_prim = axis(prim, 1)
    temps_sec = axis(sec, 1)

    # tempsmortcumul = axis(prim, 3)
    # temeperatue = axis(prim, 4)

    # data processing
    coincidancetab = coincidance(temps_sec, temps_prim, 0.01)

     histogramme(tension, 100, plt)

    # ploting
    plt.show()


if __name__ == '__main__':
    main()




















