

import numpy as np
import matplotlib.pyplot as plt
a = np.genfromtxt('muon.txt', skip_header=1, delimiter=',', dtype=int)
ax = a[:,0:2]
plt.plot(ax)
plt.show()
#print(ax)












#names = (arr[0])
#for n in range(len(names)):
# plt.plot(arr[n], arr[n])
#plt.legend()
#for i in a:
#a = [0]
#plt.scatter(['x'], ['y'])
#plt.plot(a)
#plt.show()







