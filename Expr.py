def Expr(a, n):
    if n==0:
        return 1#se n for 0 caso base
    elif (n%2) ==1: # se n for impar
        return  Expr(a, n-1)*a
    else:#se n for par
        p= Expr(a, n/2)
        return p*p
