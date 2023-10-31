
#Comb(np, t): 
# para i ← t..n incl.: 
 #P[np] ← i 
 #se np = q: 
 #escreve(P) 
 #senão: 
 #Comb(np+1, i+1)
#ler (n, q) 
#Comb(1,1
def Combinacao(np,t):
    for i in range(t, n + 1):
        P[np] = i
        if np == q:
            print(P)
        else:
           Combinacao(np+1,t+1)
           
#entrada de dados
n = int(input("Digite n: "))
q = int(input("Digite q: "))
S = [False] * (n + 1)
P = [0] * (n + 1)
Combinacao(1,1)


                
