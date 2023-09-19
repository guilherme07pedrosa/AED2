def cria_matriz(num_linhas, num_colunas):
    matriz = []
    for _ in range(num_linhas):
        linha = [-1] * num_colunas  # Inicializa uma linha com -1 (ou qualquer valor adequado)
        matriz.append(linha)
    return matriz

def Moedas(p, n, T):
    if (n < 0) or (p == 0):
        return 0
    elif n == 0:
        return 1
    else:
        if T[p - 1][n] == -1:
            T[p - 1][n] = Moedas(p, n - V[p - 1], T) + Moedas(p - 1, n, T)
        return T[p - 1][n]

V = [1, 5, 10]
p = len(V)
n = 11
T = cria_matriz(p + 1, n + 1)  # Adicione +1 aos tamanhos para acomodar índices de 0 a p e de 0 a n

total_maneras = Moedas(p, n, T)

# Imprimir a matriz T com formatação
for linha in T:
    for elemento in linha:
        print(f'{elemento:4}', end=" ")  # Use f-string com um campo de largura de 4 para alinhar os elementos
    print()  # Pular para a próxima linha após imprimir todos os elementos da linha atual
