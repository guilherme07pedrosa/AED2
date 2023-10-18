# Cálculo do expoente de um número, o tempo de execução e a quantidade de operações utilizando recursão e divisão e conquista
import time
def Expoente_SemDivisao_e_Conquista_Recursivo_ComDivisãoEConquista(a,b):
    passos=0
    if b==0:
        return 1,0
    if b==1:
        return a,1
    else:
        resultado, passos = Expoente_SemDivisao_e_Conquista_Recursivo_ComDivisãoEConquista(a,b//2)# Vamos guardar esse resultado para diminuir o número de chamadas recurrsivas

        if (b%2)==0: #se o expoente é par
            resultado*=resultado # estamos fazendo chamadas rcurvivas para o cálculo até n//2
            passos=passos+1
            return resultado, passos
        else: #se o resultado é ímpar 
            resultado*=resultado # fazemos chamadas recursivas até n//2 
            passos=passos+1   
            return a*resultado, passos+1 #multiplicamos o resultado por "a" devido a este ser ímpar
        

# Resultados
print("\nRESULTADOS")
resultado, passos = Expoente_SemDivisao_e_Conquista_Recursivo_ComDivisãoEConquista(9, 7)
print("\nResultado da exponenciação por recursão: ", resultado)
print("\nNúmero de operações para o cálculo do exponencial  utilizando recursão: ",passos)
tempo_inicio = time.time()
print("\nTempo de execução para o cálculo do exponencial utilizando recursão", tempo_inicio)
