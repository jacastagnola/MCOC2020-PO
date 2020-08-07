

from scipy import matrix, rand
from time import perf_counter

Ns=[2,5,10,12,15,20,30,40,45,50,55,60,75,100,125,160,200,250,350,500,600,800,1000,2000,5000,10000]

corridas = 10

for i in range(corridas):
    
    delta_t=[] 
    memoria=[] 
    
    nombre=(f"matmul{i}.txt")
    archivo= open (nombre,"w")
    
    
    for N in Ns:
        
        print(f"N={N}")
        
        M_A= rand(N,N)
        M_B= rand(N,N)
        
        t1=perf_counter()
        M_C= M_A@M_B
        t2=perf_counter()
        
        dt= t2-t1
        
        tamaño= 3* (N**2)*8 
        delta_t.append(dt)
        memoria.append(tamaño)
        
        archivo.write(f"{N} {dt} {tamaño}\n")
        
        print(f"tiempo={dt} s")
        print(f"memoria utilizada={tamaño} bytes")
        
        archivo.flush()
    archivo.close()
        
        
        