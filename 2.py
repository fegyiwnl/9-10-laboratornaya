def ab():
    a = list(map(int, input().split()))
    k = len(a)
    n = abs(a[0])
    maxx = 0
    
    for i in range(1, k):
        minn = abs(a[i])
        if minn > n:
            minn = n
    
    for i in range(1, k):
        if a[i] >= 0:
            pass
        elif a[i] < a[i-1]:
            maxx = a[i]

    return minn, maxx    
        
print(ab())
