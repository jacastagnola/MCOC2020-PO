import numpy as np


def mimatmul(A,B):
    

        
    A, B = np.array(A), np.array(B)
    filas_A, columnas_B = A.shape
    filas_B, columnas_B = B.shape
    resultado = np.zeros([filas_A, columnas_B])
    
  
    
    
    for i in range(filas_A):
        for j in range(columnas_B):
            for k in range(filas_B):
                resultado[i,j]+= A[i,k] * B[k,j]
            
    return resultado  

