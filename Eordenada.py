
def Eordenada(lista):
    for i in range(0, len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False  # Se algum elemento estiver fora de ordem, a lista não está ordenada
    return True  # Se chegou até aqui, a lista está ordenada
