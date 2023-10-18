#Distancia de edição dada uma string Dados dois strings A e B, quer-se determinar a menor sequência de operações para transformar A em B.


import numpy as np
#Versão BottomUp
def DistanciaEdicaoBottomUp(A,B):   #Dados: Strings A e B, com |A| = n e |B| = m

    n=len(A)                                                 #tamanho de A
    m=len(B)                                                 #tamanho de B
    D = [[0] * (m + 1) for _ in range(n + 1)]                #Matriz de D com elementos 0
    for i in range(n+1):                                     #para i ← 0 até n incl.:
        D[i][0]=i                                            #D[i, 0] ← i                                           1 - CASO BASE PARA QUANDO A STRING A ESTÁ VAZIA
                                                             #                                                      2-OS ESTADOS SÃO REPRESENTADOS PELOS ÍNDICES i e j QUE PERCORREM OS STRINGS
    for j in range (m+1):                                    #para j ← 0 até m incl.:
        D[0][j]=j                                            #D[0, j] ← j                                           1- CASO BASE PARA QUANDO A STRING B ESTA VAZIA
    for i in range (1,n+1):                                  #para i ← 1 até n incl.:
        for j in range(1,m+1):                               #para j 1 até m incl.:
            if A[i-1]==B[j-1]:                               #A[i]==se A[i] = B[j]):
                D[i][j]=D[i-1][j-1]                          #D[i, j] ← D[i-1, j-1] 3-RECORRÊNCIA PARA CARACTERES IGUAIS
            else:
                D[i][j]= min(D[i-1][j-1], D[i-1][j], D[i][j-1])+1 #D[i, j] ← min(D[i-1, j-1],D[i-1, j], D[i, j-1])+1 3-RECORRÊNCIA PARA CARACTERES DIFERENTES
    return D[n][m],np.array(D)


#Versão TopDown

def ImprimeMatriz(D):
    for row in D:
        print(row)



def DistanciaEdicaoTopDown(A,B,D):            #Dados: Strings A e B, com |A| = n e |B| = m

    n=len(A)                                #tamanho de A /ESTADOS QUE REPRESENTAM O NUMERO DE CARACTERES DE A e B
    m=len(B)                                #tamanho de B
    

    if n==0:                                #CASO BASE
        return m                            #retorno do caso base
    if m==0:                                #CASO BASE
        return n                            #retorno do caso base

   # Verifica se o resultado já foi calculado e armazenado na matriz de tabelamanto
    if D[n][m] != -1:
        return D[n][m]

    if A[n-1]==B[m-1]:                       #Seguindo o raciocinio do exemplo BottomUp disponibilizado no slide
        D[n][m] = DistanciaEdicaoTopDown(A[:n - 1], B[:m - 1],D)# Chamada recursiva// RECCORRÊNCIA SE A[:N-1]==B[:M+1] NA FAZ NADA
        
    else:                                    # SE NÃO,  ESCOLHE-SE O MÍMIMO ENTRE INSERÇÃO, DELEÇÃO OU SUBSTITUIÇÃO +1
        insercao = 1+DistanciaEdicaoTopDown(A, B[:m-1],D)
        delecao  = 1+DistanciaEdicaoTopDown(A[:n-1], B,D)
        substituicao=1+ DistanciaEdicaoTopDown(A[:n-1], B[:m-1],D)
        D[n][m] = min(insercao,delecao,substituicao)

    
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
D= [[-1]*(m+1) for _ in range(n+1)]     #Matriz de tabelamento tive que passar como referência na função para imprimir no final
resultadoTopDown=DistanciaEdicaoTopDown(A,B,D)
print("\n Resultado TopDown ","\n",resultadoTopDown)
print("\n matriz de tabelamento na abordagem TopDown")
ImprimeMatriz(D)
