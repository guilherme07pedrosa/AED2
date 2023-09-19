

def CriaVetorMarcado(n):
    T=[]
    for i in range (0,n+1):
        T.append(-1)
    return T



def FibComMemoria(n):
    if n < 2:
        return(n)
    elif  T[n] == -1:
        T[n] = Fib(n-1)+ Fib (n-2)
        return T[n]


