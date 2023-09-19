from Fatorial_Recursão import Fatorial_Recursão
from Fib import Fib
from mostrar_menu import mostrar_menu
from Hanoi import Hanoi
from  fatorial import fatorial
from Expr import Expr
from criar_lista import criar_lista
from Eordenada import Eordenada 
from busca_binaria import busca_binaria
from MaxMin import MaxMin
def main():
    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            numero = int(input("Digite um número para calcular o fatorial: "))
            resultado = Fatorial_Recursão(numero)
            print(f'O fatorial de {numero} é {resultado}')
        elif escolha == "2":
            numero = int(input("Digite um número para calcular o Fibonacci: "))
            resultado = Fib(numero)
            print(f'O Fibonacci de {numero} é {resultado}')
        elif escolha == "3":
            numero = int(input("Digite o número de discos: "))
            Hanoi(numero, 'Torre A', 'Torre B', 'Torre C')
        elif escolha == "4":
            numero = int(input("Digite um número para o cálculo do fatorial: "))
            print(f"Calculando o fatorial de {numero}")
            resultado = fatorial(numero)
        elif escolha == "5":
            resultado = Expr(int(input("\nDigite um número para a base: ")), int(input("\nDigite um número para o expoente: ")))
            print(f'O Resultado  é {resultado}')
        elif escolha == "6":
            nova_lista = criar_lista()
            while True:
                entrada=(input("Digite um número inteiro: ou q para sair "))
                if entrada=="q":
                    break
                try:
                    numero=int(entrada)
                    nova_lista.append(numero)
                except ValueError:
                    print("Entrada inválida. Por favor, digite um número inteiro válido.")
            if Eordenada(nova_lista)==True:
                numero = int(input("Digite o número procurado: "))
                print("\nElemento encontrado na posição: ", busca_binaria(nova_lista,0,len(nova_lista)-1,numero))
            else:
                print ("A lista de estar ordenada")
        elif escolha=="7":
            nova_lista = criar_lista()
            while True:
                entrada =(input("Digite os números a serem comparados: "))
                if entrada=="q":
                    break
                try:
                    numero=int(entrada)
                    nova_lista.append(numero)
                except ValueError:
                    print()
            print(MaxMin(0,len(nova_lista)-1,nova_lista))
        elif escolha == "8":
            resultado = (int(input("\nDigite o primeiro numero: ")), int(input("\nDigite o segundo numero: ")))
            print(f'O Resultado  é {resultado}')
        
        elif escolha == "q":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()


