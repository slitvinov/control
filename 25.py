import math

def L(al):
    return - 100 * (al[1] - al[0]**2)**2 - (1 - al[0])**2

def La(al):
    return [400 * al[0] * (al[1] - al[0]**2) + 2 * (1 - al[0]),
            -200 * (al[1] - al[0]**2)]

al = [-0.1, 0.1]
ep = 0.12207031e-02
i = 0
J = L(al)
while True:
    while True:
        alp = [al + ep * L1 for al, L1 in zip(al, La(al))]
        Jk = L(alp)
        if Jk >= J:
            J = Jk
            al = alp
            break
        else:
            ep /= 2
    i += 1
    if i in (1, 2, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100):
        print("%3d [%16.7e %16.7e] %.7e %.7e" % (i, *al, -J, ep))
    ep = 1
    if i == 100:
        break
