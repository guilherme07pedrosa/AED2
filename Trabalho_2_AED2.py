import random
import time

def MergeSort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)
    if (fim - inicio > 1):
        meio = (fim + inicio) // 2
        MergeSort(lista, inicio, meio)
        MergeSort(lista, meio, fim)
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

def QuickSort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)-1
    if inicio < fim:
        q = Particione(lista, inicio, fim)
        QuickSort(lista, inicio, q-1)
        QuickSort(lista,  q+1, fim)
        
   
def Particione(lista, inicio=0, fim=None):
    pivot =lista[fim]
    i = inicio
    for j in range   (inicio,fim):
        if lista[j] <= pivot:
            lista[j], lista[i] = lista[i], lista[j]
            i = i + 1
    lista[i],lista[fim] = lista[fim],lista[i]
    return (i)


#função para criar lista aleatória
def Criar_Lista_Aleatoria(tamanho, valor_minimo, valor_maximo):
    return [random.randint(valor_minimo, valor_maximo) for _ in range(tamanho)]

#teste do programa

def criar_lista_com_menor_ultimo(tamanho):
    if tamanho <= 0:
        return []

    lista = [random.randint(1, 999999) for _ in range(tamanho - 1)]  # Cria uma lista com números aleatórios
    lista.append(0)  # Adiciona 0 como o último elemento
    return lista

    
      
if __name__ == "__main__":
    
    lista = Criar_Lista_Aleatoria(5000, 0, 999999)#criação da lista
    lista_teste=criar_lista_com_menor_ultimo(5000)#criação da lista teste
    # Medição do tempo para o Merge Sort
    tempo_inicio = time.time()
    MergeSort(lista.copy())  # Copia da lista para não ordená-la antes do QuickSort
    tempo_fim = time.time()
    print("Tempo de execução do MergeSort:", tempo_fim - tempo_inicio, "segundos")
    print("\n")
    # Medição do tempo para o Quick Sort
    tempo_inicio = time.time()
    QuickSort(lista.copy())  # Copia da lista novamente para ordená-la com o QuickSort
    tempo_fim = time.time()
    print("Tempo de execução do QuickSort:", tempo_fim - tempo_inicio, "segundos")
    print("\n")
    print("Esse teste tem como tese o fato do pior caso da ordenação QuickSort ocorrer quando o pivor é\n")
    print("o menor ou o maior elemento da lista, contruimos uma lista como números aletórios e 1 a 999999 até a penúltima posição\n")
    print("cujo  o último elemento é  0\n")
    # Medição do tempo para de teste para  o Quick Sort
    tempo_inicio = time.time()
    QuickSort(lista_teste.copy())  # Copia da lista novamente para ordená-la com o QuickSort
    tempo_fim = time.time()
    print("Tempo de execução do QuickSort:", tempo_fim - tempo_inicio, "segundos")
