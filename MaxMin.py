def MaxMin(e,d,s):
    if len(s)==0:
        return -1
    if e == d:
        return (s[e], s[e])
    else: 
        if d == e+1:
            if s[e] < s[d]: 
                return (s[e], s[d])
            else:
                return (s[d], s[e])
        else:
            m = (e+d)//2
            (a_1, b_1)= MaxMin(e, m,s)
            
            (a_2, b_2)= MaxMin(m+1, d,s)
        
    return (min(a_1, a_2), max (b_1, b_2))



#nova_lista=[1,2,3,4,5]
#print(MaxMin(0,len(nova_lista)-1,nova_lista))
