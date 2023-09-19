import time
from CriaVetor import CriaVetor


def Fib_Iterativo(T):
    T[0]=0;
    T[1]=1
    for i in range (2, len(T)):
        T[i] =T[i-1]+T[i-2]
    return T

T=CriaVetor(400)
Fib_Iterativo(T)
tempo=time.time()
print (tempo)
