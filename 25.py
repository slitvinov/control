def L(al):
    return -100 * (al[1] - al[0]**2)**2 - (1 - al[0])**2


def La(al):
    return [
        400 * al[0] * (al[1] - al[0]**2) + 2 * (1 - al[0]),
        -200 * (al[1] - al[0]**2)
    ]


al = 1.2, 1.0
i = 0
J = L(al)
while i < 1000:
    ep = 1
    L1 = La(al)
    while True:
        alp = [al + ep * L1 for al, L1 in zip(al, L1)]
        Jk = L(alp)
        if Jk >= J:
            J = Jk
            al = alp
            break
        else:
            ep /= 2
    i += 1
    if i in (1, 2, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 1000):
        print("%5d [%16.7e %16.7e] %.7e %.7e" % (i, *al, -J, ep))
