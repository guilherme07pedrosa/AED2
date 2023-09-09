from Fatorial_Recursão import Fatorial_Recursão
from Fib import Fib
from mostrar_menu import mostrar_menu
from Hanoi import Hanoi
from  fatorial import fatorial
from Expr import Expr
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

        elif escolha == "q":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()


