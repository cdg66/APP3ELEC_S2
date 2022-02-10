import numpy as np
import matplotlib.pyplot as plt


def axis(array, colum):
    ret = np.array([])
    for i in range(len(array)):
        ret = np.append(ret, array[i][colum])
    return ret


def histogrammelog(x, y, width, color, plt):
    plt.hist(x, color=color, bins=np.logspace(np.log10(1), np.log10(500)), histtype='step')
    plt.xscale("log")
    #plt.step(hist, )
    #plt.step(x, (np.append( histArray, 0) / max(y)), color=color)

def histogramme(x, width, color, plt):
    histmin = np.floor(min(x))
    histmax = np.ceil(max(x)) + width
    bins = np.arange(histmin, histmax, width)
    plt.hist(x, color=color, bins=bins, histtype='step')
#    plt.show()

def annotation():
    plt.ylabel('Rate/bin[s-1]')
    plt.xlabel('Calculated SiPM peak voltage [mV]')
    plt.title("Histogramme")
    plt.legend(['All event', 'Non-coincident events','Coincident events'])

def save_image(name, fig):
    plt.figure(fig).savefig('leqf2501-gauc1102-'+name+'.png')

def coincidance(T1, T2, DT):
    TR = np.zeros(len(T1))
    dernierecoincidence = 0
    for i in range(len(T1)):

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

def trisTR(TR, tension, C):
    ret = np.zeros(len(TR))
    for i in range(0, len(TR)):
        if TR[i] == C:
            ret[i] = tension[i]
        else:
            ret[i] = 0
    return ret

def main():
    bins = 10
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


    tensionC = trisTR(coincidancetab, sec_tension, 1)
    tempsC = trisTR(coincidancetab, temps_sec, 1)
    tensionNC = trisTR(coincidancetab, sec_tension, 0)
    fig = plt.figure(1)

    # ploting
    histogrammelog(tensionC, temps_sec, bins, "red", plt)
    histogrammelog(tensionNC, temps_sec, bins, "green", plt)
    histogrammelog(sec_tension, temps_sec,  bins, "blue", plt)
    annotation()
    save_image('test', fig)
    plt.show()


if __name__ == '__main__':
    main()




















