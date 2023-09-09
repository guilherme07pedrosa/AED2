def busca_binaria(A, p, r, z):
 if r >= p:
     meio = (r + p) // 2
     if A[meio] == z: # Se z está no meio
         return meio
     elif A[meio] > z: # Se z < meio, z pode estar a esq
         return busca_binaria(A, p, meio - 1, z)
     else: #Caso contrário, z está à direita
         return busca_binaria(A, meio + 1, r, z)
 else: #Elemento não está em A
     return -1
