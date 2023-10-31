#SomaSub (ns, t): #dado conjunto C, |C|=n, 
#inteiro s 
# inteiro i ← t 
# enquanto i ≤ n e (soma + C[i]) ≤ s): 
# S[ns] ← i 
# soma ← soma + C[i] 
# se soma = s: 
 #escreve (S) 
 #senão:
 #SomaSub (ns+1, i+1) 
 #soma ← soma - C[i] 
 #i ← i + 1 
#ler(s) 
#soma ← 0 
#Ordena C 
#SomaSub (1, 1)

def Soma4quadrados(ns, t):
    global soma  # Use a variável soma como global para evitar problemas de escopo
    while t<= n and (soma + C[t]) <= s:
        S[ns] = t
        soma += C[t]
        if soma == s:
            print(S[:ns+1])  # Imprime apenas os elementos até ns
        else:
            Soma4quadrados(ns + 1, t + 1)
        soma -= C[t]
        t += 1

# Entrada de dados
s = int(input("Digite o número: "))
n = s
C = [0] * (n + 1)  # Adicione +1 para incluir o índice 0
for i in range(1, n + 1):
    C[i] = i**2
    

soma = 0
S = [0] * (n + 1)

Soma4quadrados(1, 1)

