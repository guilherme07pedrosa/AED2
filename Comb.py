def Comb(n, p):
    if (n or p)<=1:
        return -1
    if  p == 1:
        return n
    else:
        return Comb(n-1, p-1)*n/p 
