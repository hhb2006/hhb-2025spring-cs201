def dfs(i,bd,cnt):
    re = 0
    #print(vr,vc,bd[i],cnt)
    if cnt == k:
        return 1
    if i == len(bd):
        return 0
    vr.add(bd[i][0])
    vc.add(bd[i][1])
    for j in range(i+1,len(bd)):
        if bd[j][0] not in vr and bd[j][1] not in vc:
            re += dfs(j,bd,cnt+1)
    vc.remove(bd[i][1])
    vr.remove(bd[i][0])
    return re


while True:
    n, k = map(int, input().split())
    if n == -1 and k == -1:
        exit()
    space = 0
    board = []
    for r in range(n):
        line = input()
        for c in range(n):
            if line[c] == '#':
                board.append((r, c))
    res = 0
    for u in range(len(board)-k+1):
        vr, vc = set(), set()
        res += int(dfs(u, board,1))
    print(res)