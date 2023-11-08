import pdb

conjunto_de_segmentos = []

def CriaSegmento(x, y):
    segmento = [x, y]
    conjunto_de_segmentos.append(segmento)

def OrdenaSegmento():
    global conjunto_de_segmentos
    conjunto_de_segmentos = sorted(conjunto_de_segmentos, key=lambda x: x[0])

def VerificaCobertura():
    global conjunto_de_segmentos,a, b
    p = a
    #pdb.set_trace()
    cobre = True
    
    OrdenaSegmento()
    
    for segmento in conjunto_de_segmentos:
        ci, fi = segmento
        
        if p < b:
            if ci > p:
                cobre = False
            elif fi > p:
                p = fi
        
    if p < b:
        cobre = False
    return cobre


#CoberturaMinima(): 
#Ordenar S por ci; R ← Ø; 
#c0 ← -∞; f0 ← -∞; cn+1 ← ∞; fn+1 ← ∞; 
#p ← a; q ← 0; 
#para i ← 1..n+1 incl.: 
#se ci > p: 
#R ← R + (cq,fq); p ← fq; q ← i; 
#se (p ≥ b): 
#parar loop 
#senão se fi > fq: 
#q ← i 
#escrever ( R )


def CoberturaMinima():
    global conjunto_de_segmentos, resultado,a
    R = []  # Inicializar R como uma lista vazia
    c0, f0 = -float("inf"), -float("inf")#c0 e f0 recebendo o menor número possivel
    cn1, fn1 = float("inf"), float("inf")#cn1,fn1 recebendo o maior num possivel
    p=a
    q=0
    OrdenaSegmento()#ordena
    if VerificaCobertura()==True:#verifica a cobertura
        for i in range(len(conjunto_de_segmentos)+1):
            ci, fi = conjunto_de_segmentos[i - 1]
            if ci > p:
                R.append((ci, fi))
                p = fi
                q = i
                if p >= b:
                    break

                elif fi > f0:
                    q = i
        return R
    else:
        return ("Nao tem cobertura")


# Exemplo de uso:
CriaSegmento(1, 5)
CriaSegmento(2, 6)
CriaSegmento(3, 7)
CriaSegmento(6, 10)


a = 3
b = 9
teste= CoberturaMinima()
resultado= VerificaCobertura()
resultado_2=CoberturaMinima()
print("Cobre todos os segmentos:", resultado)
print("R:", resultado_2)
