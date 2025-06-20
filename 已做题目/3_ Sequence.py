import heapq


t = int(input())
for _ in range(t):
    m, n = map(int, input().split())
    sums = sorted(list(map(int, input().split())))
    for _ in range(m - 1):
        seq = sorted(list(map(int, input().split())))
        hp = [(sums[_] + seq[0], _, 0) for _ in range(n)]
        heapq.heapify(hp)
        res = []
        for _ in range(n):
            addup, i, j = heapq.heappop(hp)
            res.append(addup)
            if j < n-1:
                heapq.heappush(hp, (sums[i] + seq[j+1], i, j+1))
        sums = res
    print(*sums)
