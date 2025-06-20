from functools import lru_cache


@lru_cache(maxsize = None)
def dfs(n, ind, is_used):
    global vals
    l1 = l2 = r1 = r2 = 0
    if ind * 2 + 1 < n:
        l1 = dfs(n, ind * 2 + 1, 0)
        l2 = dfs(n, ind * 2 + 1, 1)
    if ind * 2 + 2 < n:
        r1 = dfs(n, ind * 2 + 2, 0)
        r2 = dfs(n, ind * 2 + 2, 1)
    if is_used:
        return vals[ind] + l1 + r1
    return max(l1, l2) + max(r1, r2)


N = int(input())
vals = list(map(int, input().split()))
print(max(dfs(N, 0, 1), dfs(N, 0, 0)))