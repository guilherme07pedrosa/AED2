def fatorial(n, nivel=0):
    if n == 0:
        print(f"Nível {nivel}: fatorial(0) = 1")
        return 1
    else:
        print(f"Nível {nivel}: fatorial({n}) = {n} * fatorial({n-1})")
        resultado = n * fatorial(n - 1, nivel + 1)
        print(f"Nível {nivel}: fatorial({n}) = {n} * {resultado} = {n * resultado}")
        return resultado



