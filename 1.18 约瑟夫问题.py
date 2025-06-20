while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    a = list(range(1, n+1))
    p = 0
    while len(a) > 1:
        ind  = (p+m-1) % len(a)
        a.pop(ind)
        p = ind
    print(a[0])

# http://cs101.openjudge.cn/25dsapre/02746/