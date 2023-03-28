import math

def L(al):
    return math.sin(al)**2 * math.cos(al)

def La(al):
    return 2 * math.sin(al) * math.cos(al)**2 - math.sin(al)**3

def Laa(al):
    return 2 * math.cos(al)**3 - 7 * math.sin(al)**2 * math.cos(al)


al = 0.0001
ep = 1
i = 0
J = L(al)
while True:
    while True:
        L1 = La(al)
        L2 = Laa(al)
        if L2 < 0:
            alp = al - ep * La(al)/Laa(al)
        else:
            alp = al + ep * L1
        Jk = L(alp)
        if Jk >= J:
            J = Jk
            al = alp
            break
        else:
            ep /= 2
    i += 1
    print("%2d %.7e %.1f" % (i, J, ep))    
    ep = 1
    if i == 10:
        break
