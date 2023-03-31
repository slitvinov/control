def L(al):
    return -100 * (al[1] - al[0]**2)**2 - (1 - al[0])**2


def La(al):
    return [
        400 * al[0] * (al[1] - al[0]**2) + 2 * (1 - al[0]),
        -200 * (al[1] - al[0]**2)
    ]


def Laa(al):
    xx = 400 * (al[1] - al[0]**2) - 800 * al[0]**2 - 2
    xy = 400 * al[0]
    yy = -200
    return xx, xy, yy


al = 1.2, 1.0
i = 0
J = L(al)
while i < 10:
    ep = 1
    L1x, L1y = La(al)
    L2xx, L2xy, L2yy = Laa(al)
    D = L2xx*L2yy-L2xy**2
    delta = [(L1x*L2yy-L1y*L2xy)/D, -(L1x*L2xy-L1y*L2xx)/D]
    while i < 10:
        if D < 0:
            alp = [al - ep * delta for al, delta in zip(al, delta)]
        else:
            alp = [al + ep * L1 for al, L1 in zip(al, (L1x, L1y))]
        Jk = L(alp)
        if Jk >= J:
            J = Jk
            al = alp
            break
        else:
            ep /= 2
    i += 1
    print("%5d [%16.7e %16.7e] %.7e %.7e" % (i, *al, -J, ep))
