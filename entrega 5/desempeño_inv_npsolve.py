

from time import perf_counter
import scipy as sp 
import numpy as np
from scipy.linalg import inv
from numpy import float32
from matrizlaplaciana import matriz_laplaciana



NP = [2, 5, 10,
    12, 15, 20,
    30, 40, 45, 
    50, 55, 60, 
    75, 100, 125, 
    160, 200, 250, 
    350, 500, 600, 
    800, 1000, 2000,
    5000, 10000] 

NCorridas=5

nombre_archivos=["A_invB_inv.txt", "A_invB_npSolve.txt"]

files= [open(nombre_archivo, 'w') for nombre_archivo in nombre_archivos]
 
#lista para guardar tiempos       
for N in NP:
    dts=np.zeros((NCorridas, len(files)))
    print(f"N={N}")
    
    #metodo 1 invirtiendo y multiplicando
    for i in range(NCorridas):
        print(f"i={i}")
        A = matriz_laplaciana(N)
        B = np.ones(N)
        t1 = perf_counter()
        A_inv = np.linalg.inv(A)
        A_invB = A_inv*B
        t2 = perf_counter()
        dt= t2- t1
        dts[i][0] = dt
        
        #usando np.linalg.solve
        A = matriz_laplaciana(N)
        B = np.ones(N)
        t1 = perf_counter()
        A_invB = np.linalg.solve(A, B)
        t2 = perf_counter()
        dt= t2- t1
        dts[i][1] = dt
        
    print("dts: ", dts)
    
    dts_mean = [np.mean(dts[i,j]) for j in range(len(files))]
    
    print("dts_promedio: ", dts_mean)
    
    for j in range(len(files)):
        files[j].write(f"{N} {dts_mean[j]}\n")
        files[j].flush()
        
[file.close() for file in files]