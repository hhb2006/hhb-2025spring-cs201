def find_second(table, row, col):
    dic = {}
    for i in range(row):
        for j in range(col):
            player = table[i][j]
            if player not in dic:
                dic[player] = 1
            else:
                dic[player] += 1
    lis = [(name, points) for name, points in dic.items()]
    dic.clear()
    lis.sort(key=lambda x: x[-1], reverse=True)
    tgt = lis[0][-1]
    res = []
    start = 0
    for i in range(len(lis)):
        name, points = lis[i]
        if points != tgt:
            tgt = points
            start = i
            break
    for j in range(start, len(lis)):
        name, points = lis[j]
        if points == tgt:
            res.append(name)
        else:
            break

    print(*sorted(res))
    return


while True:
    n, m = map(int, input().split())
    if n == m == 0:
        exit()
    rankings = [list(map(int, input().split())) for _ in range(n)]
    find_second(rankings, n, m)