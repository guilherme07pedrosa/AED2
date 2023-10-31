
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
def Arranjo(np):
    for i in range(1, n + 1):
        if not S[i]:
            P[np] = i
            S[i] = True
            if np == q:
                print(P)
            else:
                Arranjo(np + 1)
            S[i] = False

n = int(input("Digite n: "))
q = int(input("Digite q: "))
S = [False] * (n + 1)
P = [0] * (n + 1)
Arranjo(1)


                
