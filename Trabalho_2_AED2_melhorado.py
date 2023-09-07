import random
import time


def mergesort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)
    if (fim - inicio > 1):
        meio = (fim + inicio) // 2
        mergesort(lista, inicio, meio)
        mergesort(lista, meio, fim)
        merge(lista, inicio, meio, fim)
   

def merge(lista, inicio, meio, fim):
    left = lista[inicio:meio]
    right = lista[meio:fim]
    topo_left, topo_right = 0, 0
    for k in range(inicio, fim):
        if topo_left < len(left) and (topo_right >= len(right) or left[topo_left] <= right[topo_right]):
            lista[k] = left[topo_left]
            topo_left += 1
        else:
            lista[k] = right[topo_right]
            topo_right += 1

def quicksort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)-1
    if inicio < fim:
        q = particione(lista, inicio, fim)
        quicksort(lista, inicio, q-1)
        quicksort(lista,  q+1, fim)
        
   
def particione(lista, inicio=0, fim=None):
    pivot = lista[fim]
    i = inicio
    for j in range(inicio, fim):
        if lista[j] <= pivot:
            lista[j], lista[i] = lista[i], lista[j]
            i += 1
    lista[i], lista[fim] = lista[fim], lista[i]
    return i


# Função para criar lista aleatória
def criar_lista_aleatoria(tamanho, valor_minimo, valor_maximo):
    return [random.randint(valor_minimo, valor_maximo) for _ in range(tamanho)]

# Teste do programa

def criar_lista_com_menor_ultimo(tamanho):
    if tamanho <= 0:
        return []

    lista = [random.randint(1, 999999) for _ in range(tamanho - 1)]  # Cria uma lista com números aleatórios
    lista.append(0)  # Adiciona 0 como o último elemento
    return lista

def programa_original():
    lista = criar_lista_aleatoria(5000, 0, 999999)
    lista_teste = criar_lista_com_menor_ultimo(5000)
    
    # Medição do tempo para o Merge Sort
    tempo_inicio = time.time()
    mergesort(lista.copy())  # Copia da lista para não ordená-la antes do QuickSort
    tempo_fim = time.time()
    print("Tempo de execução do MergeSort:", tempo_fim - tempo_inicio, "segundos")
    print("\n")
    
    # Medição do tempo para o Quick Sort
    tempo_inicio = time.time()
    quicksort(lista.copy())  # Copia da lista novamente para ordená-la com o QuickSort
    tempo_fim = time.time()
    print("Tempo de execução do QuickSort:", tempo_fim - tempo_inicio, "segundos")
    print("\n")
    print("Esse teste tem como tese o fato do pior caso da ordenação QuickSort ocorrer quando o pivor é\n")
    print("o menor ou o maior elemento da lista, construímos uma lista com números aleatórios e 1 a 999999 até a penúltima posição\n")
    print("cujo último elemento é 0\n")
    
    # Medição do tempo para de teste para o Quick Sort
    tempo_inicio = time.time()
    quicksort(lista_teste.copy())  # Copia da lista novamente para ordená-la com o QuickSort
    tempo_fim = time.time()
    print("Tempo de execução do QuickSort na lista de teste:", tempo_fim - tempo_inicio, "segundos")

def programa_melhorado_pelo_gpt():
    lista = None
    lista_teste = None
    
    while True:
        menu()
        opcao = input("Digite o número da opção desejada: ")

        if opcao == '1':
            lista = criar_lista_aleatoria(5000, 0, 999999)
            print("Lista aleatória criada!")

        elif opcao == '2':
            lista_teste = criar_lista_com_menor_ultimo(5000)
            print("Lista de teste criada!")

        elif opcao == '3':
            if lista is not None:
                tempo_inicio = time.time()
                mergesort(lista.copy())
                tempo_fim = time.time()
                print("Tempo de execução do MergeSort:", tempo_fim - tempo_inicio, "segundos")
            else:
                print("Você precisa criar uma lista antes de executar o MergeSort.")

        elif opcao == '4':
            if lista is not None:
                tempo_inicio = time.time()
                quicksort(lista.copy())
                tempo_fim = time.time()
                print("Tempo de execução do QuickSort:", tempo_fim - tempo_inicio, "segundos")
            else:
                print("Você precisa criar uma lista antes de executar o QuickSort.")
            
        elif opcao == '5':
            if lista_teste is not None:
                tempo_inicio = time.time()
                quicksort(lista_teste.copy())
                tempo_fim = time.time()
                print("Tempo de execução do QuickSort com lista de teste:", tempo_fim - tempo_inicio, "segundos")
            else:
                print("Você precisa criar uma lista de teste antes de executar o QuickSort.")

        elif opcao == '6':
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")

def menu():
    print("Selecione uma opção:")
    print("1. Criar Lista Aleatória")
    print("2. Criar Lista de Teste")
    print("3. Executar MergeSort")
    print("4. Executar QuickSort")
    print("5. Executar QuickSort na Lista de Teste")
    print("6. Sair")

def main():
    while True:
        menu()
        opcao = input("Digite o número da opção desejada: ")

        if opcao == '1':
            programa_original()
        elif opcao == '2':
            programa_melhorado_pelo_gpt()
        elif opcao == '3':
            print("Saindo do programa.")
            break  # Sair do loop quando a opção '3' for selecionada
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
