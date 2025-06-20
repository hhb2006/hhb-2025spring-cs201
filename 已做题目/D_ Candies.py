import heapq


n, m = map(int, input().split())
vectors = {i: dict() for i in range(1, n + 1)}

for _ in range(m):
    k1, k2, c = map(int, input().split())
    if k2 in vectors[k1]:
        vectors[k1][k2] = min(c, vectors[k1][k2])
    else:
        vectors[k1][k2] = c

def dijkstra(graph, t):
    hp = [(0, 1)]
    vis = set()
    dist = {i: float('inf') for i in range(1, t + 1)}
    dist[1] = 0

    while hp:
        d, u = heapq.heappop(hp)
        if u in vis:
            continue
        if u == t:
            return d
        vis.add(u)

        for v in graph[u]:
            if v not in vis and graph[u][v] + d < dist[v]:
                dist[v] = graph[u][v] + d
                heapq.heappush(hp, (dist[v], v))

print(dijkstra(vectors, n))