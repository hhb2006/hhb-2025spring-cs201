import heapq


def prim(n, graph):
    vis = set()
    lth = 0
    hp = [(0, 0)]
    dist = {i: float('inf') for i in range(n)}
    dist[0] = 0

    while len(vis) < n:
        edge, vertex = heapq.heappop(hp)
        if vertex in vis:
            continue
        lth += edge
        vis.add(vertex)

        for nxt in range(n):
            if graph[vertex][nxt] != 0 and graph[vertex][nxt] < dist[nxt]:
                dist[nxt] = graph[vertex][nxt]
                heapq.heappush(hp, (dist[nxt], nxt))

    return lth


def main():
    while True:
        try:
            n = int(input())
        except EOFError:
            break

        cnt = 0
        graph = []

        while cnt < n:
            row = []
            while len(row) < n:
                inp = list(map(int, input().split()))
                row += inp
            cnt += 1
            graph.append(row)

        print(prim(n, graph))


if __name__ == '__main__':
    main()