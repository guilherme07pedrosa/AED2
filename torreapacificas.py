def torreapacificas(np, l, c):
    if np == 8:
        if p[c] == l:
            print(p)
           
            
    else:
        for i in range(8):
            if not s[i]:
                p[np] = i
                s[i] = True
                torreapacificas(np + 1, l, c)
                s[i] = False

s = [False] * 8
p = [0] * 8

torreapacificas(0, 7, 7)

