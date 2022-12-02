def lol():
    a = list(map(int, input().split())) # задается переменная в которую записывается список - list(), затем, чтобы объединить 2 действия пишется map(), а в мап через , задаем эти аргументы, а именно int( integer) и input()(ввод), чтобы ввод был чрез пробелы пишется split() через точку рядом с input
    k = len(a) # длина строки или списка и тд
    c = sum(a) # сумма
    null_p = 0 # переменная к положительным
    null_o = 0 # переменная к отрицательным

    for i in range(1, k): # цикл поиска первого положительного
        if a[i] > 0:
            null_p = i
            break

    for i in range(1, k): # цикл поиска последнего отрицательного
        if a[i] < 0:
            null_o = i

    if null_p == 0 and null_o == 0:
        return 0, 0
    elif null_p == 0 and null_o > 0:
        return 0, null_o + 1
    else:
        return null_p + 1, null_o + 1

print(lol()) # обязательно скобки
