def cria_matriz(num_linhas, num_colunas):
    matriz = []
    for _ in range(num_linhas):
        linha = [0] * num_colunas  # Inicializa uma linha com zeros
        matriz.append(linha)
    return matriz

def  Moedas (p, q):
    if  (q < 0) or (p ==0):
        return 0
    elif q == 0:
        return 1
    else:
        if T[p, q] == -1:
            T[p, q]=Moedas(p,q-V[p])+Moedas(p-1,q)
        return T[p, q]
