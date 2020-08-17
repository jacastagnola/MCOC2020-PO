

from time import perf_counter
import scipy as sp 
import numpy as np
from scipy.linalg import inv
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

nombre_archivos=["A_invB_inv.txt", "A_invB_npSolve.txt", "A_invB_spSolve.txt", "A_invB_spSolve_symetric.txt" , "A_invB_spSolve_pos.txt", "A_invB_spSolve_pos_overwrite.txt"]


files= [open(archivo, 'w') for archivo in nombre_archivos]
      
for N in NP:
    dts=np.zeros((NCorridas, len(files)))
    print(f"N={N}")
   
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
        
        A = matriz_laplaciana(N)
        B = np.ones(N)
        t1 = perf_counter()
        A_inv = np.linalg.inv(A)
        A_invB = np.linalg.solve(A, B)
        t2 = perf_counter()
        dt= t2- t1
        dts[i][1] = dt
        
        A = matriz_laplaciana(N) 
        B = np.ones(N)
        t1 = perf_counter()
        A_inv = np.linalg.inv(A)
        A_invB = sp.linalg.solve(A, B)
        t2 = perf_counter()
        dt= t2- t1
        dts[i][2] = dt
        
        A = matriz_laplaciana(N) 
        B = np.ones(N)
        t1 = perf_counter()
        A_inv = np.linalg.inv(A)
        A_invB = sp.linalg.solve(A, B, assume_a = "sym")
        t2 = perf_counter()
        dt= t2- t1
        dts[i][3] = dt
        
        A = matriz_laplaciana(N) 
        B = np.ones(N)
        t1 = perf_counter()
        A_inv = np.linalg.inv(A)
        A_invB = sp.linalg.solve(A, B, assume_a = "pos")
        t2 = perf_counter()
        dt= t2- t1
        dts[i][4] = dt
        
        A = matriz_laplaciana(N) 
        B = np.ones(N)
        t1 = perf_counter()
        A_inv = np.linalg.inv(A)
        A_invB = sp.linalg.solve(A, B, assume_a = "pos", overwrite_a=True, overwrite_b=True)
        t2 = perf_counter()
        dt= t2- t1
        dts[i][5] = dt
        
    print("dts: ", dts)
    
    dts_prom = [np.mean(dts[i,j]) for j in range(len(files))]
    
    print("dts_promedio: ", dts_prom)
    
    for j in range(len(files)): 
        files[j].write(f"{N} {dts_prom[j]}\n")
        files[j].flush()
        
[file.close() for file in files]

