def has_cycle(u):
    if sign[u] == 1:
        return True
    if sign[u] == 2:
        return False

    sign[u] = 1
    for v in graph[u]:
        if has_cycle(v):
            return True
    sign[u] = 2
    return False



T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    graph = {_: [] for _ in range(n)}

    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        graph[a].append(b)

    sign = [0] * n
    for vertex in graph:
        if has_cycle(vertex):
            print('Yes')
            break
    else:
        print('No')
