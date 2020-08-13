
import scipy as sc
import numpy as np
from scipy import matrix, rand ,linalg
from time import perf_counter

from matrizlaplaciana import matriz_laplaciana


Ns = [2, 5, 10, 12, 15, 20, 30, 40, 45, 50, 55, 60, 75, 100,
      125, 160, 200, 250, 350, 500, 600, 800, 1000, 2000,5000, 10000]
  
delta_t = [] 
memoria = [] 
    
nombre = f"datos_timing_inv_caso_3_single.txt"
archivo = open(nombre, "w")
    
for N in Ns:    
    print(f"N={N}")
        
    # crear matriz
    A = matriz_laplaciana(N, np.single)
    
    # calcular la inversa
    t1 = perf_counter()     
    A_inv = sc.linalg.inv(A, overwrite_a=True)
    t2 = perf_counter()
    
    # obtener tiempo
    dt = t2-t1
    delta_t.append(dt)

    # obtener tamano
    tamaño = A.itemsize*(N**2)
    memoria.append(tamaño)    
        
    # escribir en el archivo
    archivo.write(f"{N} {dt} {tamaño}\n")
    
    print(A_inv.dtype)  
    # print(f"tiempo={dt} s")
    # print(f"memoria utilizada={tamaño} bytes")
        
    archivo.flush()
archivo.close()
