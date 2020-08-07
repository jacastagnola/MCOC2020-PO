from psutil import virtual_memory
import scipy as sp
import matplotlib.pyplot as plt
import numpy as np



xticks = [10,20,50,100,200,500,1000,2000,5000,10000,20000]
yticks = [0.1e-3,1e-3,10e-3,0.1,1,10,60,600]
ylabels=["0.1 ms","1 ms","10 ms","0.1 s","1 s","10 s","1 min", "10 min"]
yticks2=[10**i for i in range(3, 11)]
ylabels2=["1 KB","10 KB","100 KB","1 MB","10 MB", "100 MB","1 GB", "10 GB"]

fig = plt.figure()  # crea la figura
ax = fig.add_subplot(2,1,1)

for i in range(10):
    data = np.loadtxt(f'matmul{i}.txt')
    ax.plot(data[:,0], data[:,1],".-")

ax.set_xscale('log')
ax.set_yscale("log")

ax.set_xticks(xticks)
ax.set_xticklabels(['' for _ in range(len(xticks))])

ax.set_yticks(yticks)
ax.set_yticklabels(ylabels)

ax.minorticks_off()
ax.grid()

ax.set_ylabel('Tiempo Transcurrido (s)')
ax.set_title('Rendimiento A@B')


# segundo grafico
ax2 = fig.add_subplot(2,1,2)

data = np.loadtxt(f'matmul{i}.txt')
ax2.plot(data[:,0], data[:,2],".-")


ax2.set_yscale("log")
ax2.set_xscale("log")

ax2.set_xticks(xticks)
ax2.set_xticklabels(xticks)
for tick in ax2.get_xticklabels():
    tick.set_rotation(45)

ax2.set_yticks(yticks2) 
ax2.set_yticklabels(ylabels2)


ax2.set_xlabel("Tamaño de Matriz")
ax2.set_ylabel("Uso de memoria")


ax2.axhline(virtual_memory().total, linestyle='--', color='black')
ax2.set_ylim([10, 10**11])

ax2.grid()
ax2.minorticks_off()
fig.savefig('Grafico Rendimiento A@B.png')











