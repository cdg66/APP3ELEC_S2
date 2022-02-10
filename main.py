import numpy as np
import matplotlib.pyplot as plt


'''def integration(x, y):
    integral = 0
    for i in range(len(x)):
        integral = integral + ((x[i+1] - x[i])*y[i])
    print(integral)'''

def histogrammelog_tempsmort(x, y, width, tempsmorttotal, color, plt, figtemp, fig):
    plt.figure(figtemp)
    Ylog, Xlog, bs  = plt.hist(x, color=color, bins=np.logspace(np.log10(10), np.log10(500), 20), histtype='step')
    Ylog = np.append(Ylog, 0)
    Ylog = (Ylog/ np.ceil(max(y) - tempsmorttotal))*1000
    plt.close(figtemp)
    plt.figure(fig)
    plt.step(Xlog, Ylog, color=color)
    plt.xscale("log")


def histogrammelog(x, y, color, plt, figtemp, fig):
    plt.figure(figtemp)
    Ylog, Xlog, bs  = plt.hist(x, color=color, bins=np.logspace(np.log10(10), np.log10(500), 20), histtype='step')
    Ylog = np.append(Ylog, 0)
    Ylog = (Ylog/ np.ceil(max(y)))*1000
    plt.close()
    plt.figure(fig)
    plt.step(Xlog, Ylog, color=color)
    plt.xscale("log")

def histogramme(x, width, color, plt, fig):
    histmin = np.floor(min(x))
    histmax = np.ceil(max(x)) + width
    bins = np.arange(histmin, histmax, width)
    plt.hist(x, color=color, bins=bins, histtype='step')

def annotation(name):
    plt.ylabel('Rate/bin[s-1]')
    plt.xlabel('Calculated SiPM peak voltage [mV]')
    plt.title(name)
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
    # ----------------------------------reteving datas------------------------------------
    temps_prim = np.genfromtxt('S2GE_APP3_Problematique_Detecteur_Primaire.csv', delimiter=',', dtype=float, unpack=True, usecols=(1))
    index, temps_sec, sec_tension, tempsmortcumul = np.genfromtxt('S2GE_APP3_Problematique_Detecteur_Secondaire.csv', delimiter=',', dtype=float, unpack=True, usecols=(0, 1, 2, 3))

    # ------------------------------------data processing------------------------------------
    tempsmorttotal = np.sum(tempsmortcumul)
    coincidancetab = coincidance(temps_sec, temps_prim, 0.01)
    tensionC = trisTR(coincidancetab, sec_tension, 1)
    tempsC = trisTR(coincidancetab, temps_sec, 1)
    tensionNC = trisTR(coincidancetab, sec_tension, 0)

    # ------------------------------------ploting--------------------------------------------
    fig = plt.figure(1)
    fig2 = plt.figure(2)
    histogrammelog_tempsmort(sec_tension, temps_sec, bins, tempsmorttotal, "blue", plt, 3, 1)
    histogrammelog_tempsmort(tensionNC, temps_sec, bins, tempsmorttotal, "green", plt, 3, 1)
    histogrammelog_tempsmort(tensionC, temps_sec, bins, tempsmorttotal, "red", plt, 3, 1)

    annotation( name = 'Historgramme avec temps mort ')
    save_image('histo_avec_temps_mort', 1)

    histogrammelog(sec_tension, temps_sec, "blue", plt, 3, 2)
    histogrammelog(tensionNC, temps_sec, "green", plt, 3, 2)
    histogrammelog(tensionC, temps_sec, "red", plt, 3, 2)
    annotation( name = 'Historgramme sans temps mort ')
    save_image('histo_sans_temps', 2 )
    plt.show()


if __name__ == '__main__':
    main()




















