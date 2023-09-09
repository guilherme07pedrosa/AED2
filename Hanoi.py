def Hanoi(n, origem, trabalho, destino):
    if n == 1:
        print(f'Mova o disco 1 de {origem} para {destino}')
        return
    Hanoi(n - 1, origem, destino, trabalho)
    print(f'Mova o disco {n} de {origem} para {destino}')
    Hanoi(n - 1, trabalho, origem, destino)


