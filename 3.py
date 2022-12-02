def lol():
    a = list(map(int, input().split()))  # задается переменная в которую записывается список - list(), затем, чтобы объединить 2 действия пишется map(), а в мап через запятую задаем эти аргументы, а именно int (эinteger) и input()(ввод), чтобы ввод был чрез пробелы пишется split() через точку рядом с input
    k = len(a)  # длина строки или списка и тд
    null_p = 0  # переменная к положительным
    null_o = 0  # переменная к отрицательным

    for i in range(1, k):  # цикл поиска первого положительного
        if a[i] > 0:
            null_p = i
            break

    for i in range(1, k):  # цикл поиска последнего отрицательного
        if a[i] < 0:
            null_o = i + 1

    if null_p == 0 and a[0] > 0:
        null_p = 1

    if null_o == 0 and a[0] < 0:
        null_o = 1

    if null_p == 0 and null_o == 0:
        return 0, 0
    elif null_p == 0 and null_o > 0:
        return 0, null_o
    elif null_p >= 1 and null_o == 0:
        return null_p, 0
    else:
        return null_p, null_o

print(lol())  # обязательно скобки
