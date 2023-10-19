def part_aprox(ns, t):
    global melhor_solucao, soma, msmp, dif, tot, C, S, n

    i = t
    while i <n and (soma + C[i - 1]) < msmp:
        S[ns] = i - 1
        soma += C[i - 1]

        if abs(tot - 2 * soma) < dif:
            Guarda()
            dif = abs(tot - 2 * soma)
            msmp = max(soma, tot - soma)

        part_aprox(ns + 1, i + 1)

        soma -= C[i - 1]
        i += 1

def Guarda():
    global melhor_solucao, S
    melhor_solucao = S.copy()

# Inicialização
C = [1, 2, 3, 4]
C.sort()  # Ordena o vetor
n = len(C)
S = [-1] * (n + 1)
soma = C[0]
ns = 1
S[1] = 0
tot = sum(C)
dif = tot - 2 * C[0]
msmp = max(C[0], tot - C[0])
melhor_solucao = [-1] * (n + 1)

# Chamada da função principal
part_aprox(1, 2)

# Encontre o ponto de divisão com base na melhor solução
divisor = max(melhor_solucao)

subvetor1 = [C[i] for i in range(n) if i in melhor_solucao if i != -1]
subvetor2 = [C[i] for i in range(n) if i not in melhor_solucao]

# Divida os subvetores com base no divisor
subvetor1 = subvetor1[:divisor]
subvetor2 = subvetor2[divisor:]

print("Subvetor 1:", subvetor1)
print("Subvetor 2:", subvetor2)
