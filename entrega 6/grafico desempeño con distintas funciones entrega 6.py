
from psutil import virtual_memory
import matplotlib.pyplot as plt
import numpy as np

#ROTULO DE LOS EJES
xticks     = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]
yticks    = [0.000001, 0.1e-3, 1e-3, 10e-3, 0.1, 1, 10, 60, 600]
yticks2  = [10**i for i in range(3, 11)]
ylabels= [".","0.1 ms","1 ms","10 ms","0.1 s","1 s","10 s","1 min", "10 min"]
ylabels2 = ["1 KB","10 KB","100 KB","1 MB","10 MB", "100 MB","1 GB", "10 GB"]




fig = plt.figure(figsize=(20,20))  


ax = fig.add_subplot(2,1,1)


datos = np.loadtxt("A_invB_inv.txt")
ax.plot(datos[:,0], datos[:,1],"o-", label="A_invB_inv")
datos = np.loadtxt('A_invB_npSolve.txt')
ax.plot(datos[:,0], datos[:,1],"o-", label="A_invB_npSolve")
datos = np.loadtxt("A_invB_spSolve.txt")
ax.plot(datos[:,0], datos[:,1],"o-", label="A_invB_spSolve.txt")
datos = np.loadtxt("A_invB_spSolve_symetric.txt")
ax.plot(datos[:,0], datos[:,1],"o-", label="A_invB_spSolve_symetric.txt")
datos = np.loadtxt("A_invB_spSolve_pos.txt")
ax.plot(datos[:,0], datos[:,1],"o-", label="A_invB_spSolve_pos.txt")
datos = np.loadtxt("A_invB_spSolve_pos_overwrite.txt")
ax.plot(datos[:,0], datos[:,1],"o-", label="A_invB_spSolve_pos_overwrite.txt")



ax.set_xscale("log")
ax.set_yscale("log")


ax.set_xticks(xticks)

ax.set_xticklabels(xticks,fontsize=20)
for tick in ax.get_xticklabels():
    tick.set_rotation(45)


ax.set_yticks(yticks)

ax.set_yticklabels(ylabels,fontsize=20)

ax.grid()




ax.minorticks_on()
ax.legend(fontsize=20)
plt.tight_layout()


ax.set_title("Rendimiento resolucion de sistemas de ecuaciones con 6 diferentes solvers",fontsize=30)
ax.set_xlabel("Tamaño Matriz N",fontsize=20)
ax.set_ylabel("Tiempo Transcurrido (s)",fontsize=20)



fig.savefig("RENDIMIENTO_solvers.png")


