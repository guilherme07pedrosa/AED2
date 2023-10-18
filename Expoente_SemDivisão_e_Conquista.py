import time
def Expoente_SemDivisão_e_Conquista(a,b):
    passos=0
    for a in range(b+1):
        a=a*a
        passos=passos+1
    return a,passos

# Resultados
print("\nRESULTADOS")
resultado, passos = Expoente_SemDivisão_e_Conquista(123456789, 123456789)
print("\nResultado da exponenciação: ", resultado)
print("\nNumero de operações: ",passos)
tempo_inicio = time.time()
print("\nTempo de execução", tempo_inicio)
