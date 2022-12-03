def lol():
    a = list(map(int, input("Введите числа в массив: ").split()))
    k = len(a)
    null_p = 0
    null_o = 0

    if k == 1:
        if a[0] > 0:
            return 1, 0
        elif a[0] < 0:
            return 0, 1
        else:
            return 0, 0
    elif k == 2:
        if a[0] > 0:
            if a[1] < 0:
                return 1, 2
            else:
                return 1, 0
        elif a[0] < 0:
            if a[1] > 0:
                return 2, 1
            elif a[1] == 0:
                return 0, 1
        elif a[0] == 0:
            if a[1] == 1:
                return 2, 0
            elif a[1] < 0:
                return 0, 2
    else:
        for i in range(k):
            if a[i] > 0:
                null_p = i
                break
        if a[0] > 0:
            null_p = 1
        elif null_p > 0:
            null_p += 1

        for i in range(k):
            if a[i] < 0:
                null_o = i
        if null_o != 0:
            null_o += 1

        return null_p, null_o

print(lol())
