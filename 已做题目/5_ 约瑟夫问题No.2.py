while True:
    n, p, m = map(int, input().split())
    if n == 0 and m == 0 and p == 0:
        break
    p = (p-1) % n
    a = list(range(1, n+1))
    res = []
    while len(a) > 1:
        ind  = (p+m-1) % len(a)
        res.append(str(a.pop(ind)))
        p = ind
    res.append(str(a.pop()))
    print(','.join(res))

# http://cs101.openjudge.cn/practice/03253/