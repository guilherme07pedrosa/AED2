#Distancia de edição dada uma string Dados dois strings A e B, quer-se determinar a menor sequência de operações para transformar A em B.


import numpy as np
#Versão BottomUp
def DistanciaEdicaoBottomUp(A,B):   #Dados: Strings A e B, com |A| = n e |B| = m

    n=len(A)                                                 #tamanho de A
    m=len(B)                                                 #tamanho de B
    D = [[0] * (m + 1) for _ in range(n + 1)]                #Matriz de D com elementos 0
    for i in range(n+1):                                     #para i ← 0 até n incl.:
        D[i][0]=1                                            #D[i, 0] ← i

    for j in range (m+1):                                    #para j ← 0 até m incl.:
        D[0][j]=j                                            #D[0, j] ← j
    for i in range (1,n+1):                                  #para i ← 1 até n incl.:
        for j in range(1,m+1):                               #para j 1 até m incl.:
            if A[i-1]==B[j-1]:                               #A[i]==se A[i] = B[j]):
                D[i][j]=D[i-1][j-1]                          #D[i, j] ← D[i-1, j-1]
            else:
                D[i][j]= min(D[i-1][j-1], D[i-1][j], D[i][j-1])+1 #D[i, j] ← min(D[i-1, j-1],D[i-1, j], D[i, j-1])+1
    return D[n][m],np.array(D)


#Versão TopDown

def ImprimeMatriz(D):
    for row in D:
        print(row)



def DistanciaEdicaoTopDown(A,B):            #Dados: Strings A e B, com |A| = n e |B| = m

    n=len(A)                                #tamanho de A
    m=len(B)                                #tamanho de B
    D= [[-1]*(m+1) for _ in range(n+1)]     #Matriz de tabelamento

    if n==0:                                #caso base
        return m                            #retorno do caso base
    if m==0:                                #caso base
        return n                            #retorno do caso base

   # Verifica se o resultado já foi calculado e armazenado na matriz de tabelamanto
    if D[n][m] != -1:
        return D[n][m]

    if A[n-1]==B[m-1]:                       #Seguindo o raciocinio do exemplo BottomUp disponibilizado no slide
        D[n][m] = DistanciaEdicaoTopDown(A[:n - 1], B[:m - 1])# Chamada recursiva
    else:
        insercao = 1+DistanciaEdicaoTopDown(A, B[:m-1])
        delecao  = 1+DistanciaEdicaoTopDown(A[:n-1], B)
        substituicao=1+ DistanciaEdicaoTopDown(A[:n-1], B[:m-1])
        D[n][m] = min(insercao,delecao,substituicao)

    ImprimeMatriz(D[n][m])
    return D[n][m]                  #retorno
   













    
#caso de teste
A="ERRO" # teste do  exemplo
B="ACERTO" #teste do exemplo
n=len(A)
m=len(B)

resultadoBottomUp, MatrizBottomUp=DistanciaEdicaoBottomUp(A,B)
print("\n Impressão da Matriz de Tabelamento BottomUp")
print(MatrizBottomUp)
print("\n Resultado BottomUp","\n",resultadoBottomUp)


print("\n ############################################")

resultadoTopDown=DistanciaEdicaoTopDown(A,B)
print("\n Resultado TopDown ","\n",resultadoTopDown)

