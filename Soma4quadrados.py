def encontrar_combinacoes_quadrados(n):
    def encontrar_combinacoes_recursivas(k, inicio, soma, combinacao):
        # Função recursiva que encontra combinações de k números cujos quadrados somam a n.
        # k: número de elementos na combinação
        # inicio: valor mínimo a ser considerado para evitar duplicação
        # soma: soma dos quadrados dos elementos da combinação
        # combinacao: lista temporária para armazenar a combinação atual

        if k == 0:
            # Quando encontramos uma combinação completa (k atinge 0),
            # verificamos se a soma é igual a n.
            if soma == n:
                print(combinacao)  # Imprime a combinação válida
            return

        for i in range(inicio, int(n**0.5) + 1):
            # Itera através dos números possíveis, começando em 'inicio' até a raiz quadrada de n.
            if i * i + soma <= n:
                # Verifica se o quadrado de 'i' somado à soma atual não excede n.
                # Isso evita combinações inválidas.

                # Chamada recursiva para explorar a próxima possível adição à combinação.
                encontrar_combinacoes_recursivas(k - 1, i, soma + i * i, combinacao + [i])
                # Neste ponto, o backtracking ocorre ao explorar todas as opções para a próxima adição.

    print(f"Soluções para n = {n}:")
    for k in range(1, 5):
        # Procuramos combinações de 1 a 4 números.
        encontrar_combinacoes_recursivas(k, 1, 0, [])
        # Iniciamos a busca com k elementos, começando em 1, soma inicial 0 e uma lista vazia.

# Entrada de dados
n = int(input("Digite o número n: "))
encontrar_combinacoes_quadrados(n)
