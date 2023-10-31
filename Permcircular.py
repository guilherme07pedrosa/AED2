#Permcircular(np): 
#inteiro i 
 #para i ← 1..n-1 incl.:
 #se ~S[i]: 
 #P[np] ← i 
 #S[i] ← verdadeiro 
 #se np = n-1: 
 #escreve(P) 
 #senão: 
 #Permcircular(np+1) 
 #S[i] ← falso 
#ler (n) 
#S[*] ← falso 
#P[n] ← n 
#Permcircular(1

def Permcircular(np):
    if np == n:
        print(P)
        return

    for i in range(0, n):
        if not S[i]:
            P[np] = i
            S[i] = True
            Permcircular(np + 1)
            S[i] = False

# Entrada de dados
n = int(input("Digite n: "))

S = [False] * n
P = [0] * n
Permcircular(0)

