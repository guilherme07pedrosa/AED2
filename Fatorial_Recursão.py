#Fatorial por recursão
def Fatorial_Recursão(p):
    if p <= 0:
        return 1
    else:
        return (p* Fatorial_Recursão(p-1))


