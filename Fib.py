#Fibonacci por recursão
def Fib(p):
    if  p <= 1:
        return p
    else:
        return  (Fib(p-1) + Fib(p-2))
