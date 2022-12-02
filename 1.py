def ab():
    s = 1
    a = list(map(int, input().split()))
    for i in range(len(a)):
        if a[i] % 2 == 0:
            s *= a[i]
    return s
print(ab())
