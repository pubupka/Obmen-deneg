for number in range(1, 15):
    f = open(f'input{number}.txt')
    # исходная денежная система
    stroka = list(map(int, f.readline().split()))
    Nisx = stroka[0]
    c = [stroka[i] for i in range(1, Nisx)]
    # несчастливые числа в исходной денежной системе
    stroka = list(map(int, f.readline().split()))
    Kisx = stroka[0]
    a = sorted([stroka[i] for i in range(1, Kisx+1)], reverse=True)
    # конечная денежная система
    stroka = list(map(int, f.readline().split()))
    Nkon = stroka[0]
    d = [stroka[i] for i in range(1, Nkon)]
    # несчастливые числа в конечной денежной системе
    stroka = list(map(int, f.readline().split()))
    Kkon = stroka[0]
    b = sorted([stroka[i] for i in range(1, Kkon+1)])
    # представление денежной суммы в исходной денежной системе
    stroka = list(map(int, f.readline().split()))
    eisx = [stroka[i] for i in range(0, Nisx)]
    for i in range(len(eisx)):
        for unlucky in a:
            if eisx[i] >= unlucky:
                eisx[i] -= 1
    dengi_real = 0
    for i in range(len(eisx)):
        denga = 1
        for j in range(i, len(c)):
            denga *= c[j]
        dengi_real += denga*eisx[i]
    ekon = []
    for i in range(Nkon):
        koef = 1
        for j in range(i, len(d)):
            koef *= d[j]
        val = dengi_real // koef
        dengi_real %= koef
        ekon.append(val)
    for i in range(len(ekon)):
        for unlucky in b:
            if ekon[i] >= unlucky:
                ekon[i] += 1
    out = list(map(int, open(f'output{number}.txt').readline().split()))
    flag = True
    for i in range(len(out)):
        if out[i] != ekon[i]:
            flag = False
            break
    print(number, flag)