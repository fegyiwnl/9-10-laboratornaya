def lol():
    a = list(map(int, input("Введите числа в первый массив: ").split()))
    b = list(map(int, input("Введите числа во второй массив: ").split()))
    a1 = 0
    b1 = 0

    for i in range(len(a)):
        a1 += a[i]

    for i in range(len(b)):
        b1 += b[i]

    if a1 > b1:
        print("Второй массив оказался меньше")
        for i in range(len(b)):
            print(b[i]*10, end=" ")
    elif b1 > a1:
        print("Первый массив оказался меньше")
        for i in range(len(a)):
            print(a[i]*10, end=" ")
    else:
        print('Массивы равны')

lol()
