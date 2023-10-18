# Cálculo do expoente de um número, o tempo de execução e a quantidade de operações utilizando recursão
import time
def Expoente_SemDivisao_e_Conquista_Recursivo(a,b):
    passos=0
    if b==0:
        return 1,0
    if b==1:
        return a,1
    else:
        resultado, passos = Expoente_SemDivisao_e_Conquista_Recursivo(a, b-1)
        passos=passos+1
        a*=resultado
        passos+=1
        return a, passos

        

# Resultados
print("\nRESULTADOS")
resultado, passos = Expoente_SemDivisao_e_Conquista_Recursivo(2, 2)
print("\nResultado da exponenciação por recursão: ", resultado)
print("\nNúmero de operações para o cálculo do exponencial  utilizando recursão: ",passos)
tempo_inicio = time.time()
print("\nTempo de execução para o cálculo do exponencial utilizando recursão", tempo_inicio)
