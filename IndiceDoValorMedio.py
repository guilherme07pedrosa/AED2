#Escreva um algoritmo de divisão e conquista para encontrar a posição (índice) do elemento de valor médio em um array não ordenado com 𝑛 inteiros.
#Apresente o algoritmo em pseudocódigo, a implementação do algoritmo em Python ou C/C++ e analise a complexidade do seu algoritm

#cria um vetor vazio
vetor=[]

#loop para o usuário ir digitando valoes e ir entrando no valores e ir entrando em um vetor
while True:
    #Entrada do nnúmero 
    # Dentro do loop para entrada de números
    numero = input("\nDigite um numero ou tecla a tecla 'S' do teclado para parar: ")
    # converte 'S' para 's' e 's' mantem em 's'
    if numero.lower()=='s':                                                               
        #sai do loop
        break                                                                            
    
    #tratamento da excessão para que o usuário só digite números ou apenas a string 'S'ou 's'
    try:
        #Entrada do número e convesrão deste em float para evitar problemas no cálculo de média
        numero=float(numero)
        #Inser e uma posição a mais do vetor - o número é inserido na última posição
        vetor.append(numero)
    #se o usuário digitar uma tecla que não seja um número ou 
    except ValueError:
        print("\nDigite a tecla 'S' ou um numero ")

#imprime o vetor resultante
print ("\nVetor resultante: ", vetor)



#calcular a media
def media(v):
    soma = sum(v)
    media = soma / len(v)
    return media






# usar a tecnica de dividir para conquistar comparando a lado esquerdo e ladop direito

def IndiceDoValorMedio(v, m):
   #caso base 
    if len(v)==1:
        return 0
    
   #partição do lados
    meio=len(v)//2
    lado_E=v[:meio]
    lado_D=v[meio:]

    #Achar o indice de  menor diferença entre a média e o lado esquerdo
    #OBS: chamada recursiva até o caso base
    indice_E=IndiceDoValorMedio(lado_E, m)

    #Achar o indice de menor diferença entre a média e o lado direito
    #OBS: chamada recursiva até o caso base
    indice_D=IndiceDoValorMedio(lado_D, m)

    #Menor diferença entre os valores da esquerda
    diferenca_E=abs(v[indice_E]-m)

    #Menor diferença entre os valores da direita
    diferenca_D=abs(v[indice_D]-m)

    if diferenca_E<diferenca_D:
        return indice_E
    else:
        return (indice_D+meio)
        










# usar a tecnica de dividir para conquistar comparando a lado esquerdo e ladop direito

def IndiceDoValorMedio(v, m):
   #caso base 
    if len(v)==1:
        return 0
    
   #partição do lados
    meio=len(v)//2
    lado_E=v[:meio]
    lado_D=v[meio:]

    #Achar o indice de  menor diferença entre a média e o lado esquerdo
    #OBS: chamada recursiva até o caso base
    indice_E=IndiceDoValorMedio(lado_E, m)

    #Achar o indice de menor diferença entre a média e o lado direito
    #OBS: chamada recursiva até o caso base
    indice_D=IndiceDoValorMedio(lado_D, m)

    #Menor diferença entre os valores da esquerda
    diferenca_E=abs(v[indice_E]-m)

    #Menor diferença entre os valores da direita
    diferenca_D=abs(v[indice_D]-m)

    if diferenca_E<diferenca_D:
        return indice_E
    else:
        return (indice_D+meio)
        


# Resultados
#v = vetor
v=[1,2,3]

if len(v) == 0:
    print("\nNão é possível calcular a média de um vetor vazio.")
else:
    m = media(v)
    print("\nA média dos valores é:", m)
    indice = IndiceDoValorMedio(v, m)
    print(f"O valor mais próximo da média está no índice {indice}: {v[indice]}")
    

