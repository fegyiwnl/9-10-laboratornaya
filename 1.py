def ab(a):
    s = 1
    for i in range(len(a)):
        if a[i] % 2 == 0:
            s *= a[i]
    return s
print(ab([1, 2, 3, 4, 5, 6, 7, 8, 9]))
