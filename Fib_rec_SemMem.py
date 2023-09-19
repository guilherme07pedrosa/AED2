

def FibonacciRecursivoSemMemorizacao(n):
    if n < 2:
        return n
    else:
        return FibonacciRecursivoSemMemorizacao(n - 1) + FibonacciRecursivoSemMemorizacao(n - 2)

def CalcularFibonacciAteN(n):
    fibonacci_vetor = [0, 1]  # Inicialize o vetor com os primeiros valores de Fibonacci
    for i in range(2, n):
        fibonacci_vetor.append(FibonacciRecursivoSemMemorizacao(i))
    return fibonacci_vetor

n = 10  # Substitua pelo valor desejado
resultados = CalcularFibonacciAteN(n)
print(resultados)

