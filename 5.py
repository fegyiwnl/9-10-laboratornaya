def lol():
    a = list(map(int, input("Введите числа в первый массив: ").split()))
    b = list(map(int, input("Введите числа во второй массив: ").split()))
    c0 = 0
    c1 = 0
    maxa = a[0]
    maxb = b[0]
    mina = a[0]
    minb = b[0]

    for i in range(len(a)):
        if a[i] % 5 == 0:
            c0 = i + 1
    for i in range(len(b)):
        if b[i] % 5 == 0:
            c1 = i + 1

    if c0 < c1:
        for i in range(len(a)):
            if maxa < a[i]:
                maxa = i
        a[maxa] = 0
        print('Элементы массива с измененным максимальным числом:', *a)
        for i in range(len(b)):
            if minb > b[i]:
                minb = i
        for i in range(len(b)):
            if i > minb:
                b[i] = b[i] * 2
        print('Элементы умноженные на 2 после минимального:', *b)

    elif c0 > c1:
        for i in range(len(b)):
            if maxb < b[i]:
                maxb = i
        b[maxb] = 0
        print('Элементы массива с измененным максимальным числом:', *b)
        for i in range(len(a)):
            if mina > a[i]:
                mina = i
        for i in range(len(a)):
            if i > mina:
                a[i] = a[i] * 2
        print('Элементы умноженные на 2 после минимального:', *a)

    else:
        print("Массивы нельзя изменить")


lol()
