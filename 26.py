import math


def L(al):
    return math.sin(al)**2 * math.cos(al)


def La(al):
    return 2 * math.sin(al) * math.cos(al)**2 - math.sin(al)**3


def Laa(al):
    return 2 * math.cos(al)**3 - 7 * math.sin(al)**2 * math.cos(al)


al = 0.0001

i = 0
J = L(al)
while i < 10:
    ep = 1
    L1 = La(al)
    L2 = Laa(al)
    while True:
        alp = al + ep * (-L1 / L2 if L2 < 0 else L1)
        Jk = L(alp)
        if Jk >= J:
            J = Jk
            al = alp
            break
        else:
            ep /= 2
    i += 1
    print("%2d %.7e %.1f" % (i, J, ep))
