from collections import defaultdict
import heapq


def min_time(n, graph, nodes):
    total = {x: float('inf') for x in nodes}
    s, e = nodes[0], nodes[1]
    total[s] = 0
    hp = [(0.0, s)]    # time, node
    vis = set()

    while hp:
        t, nd = heapq.heappop(hp)
        vis.add(nd)
        if nd == e:
            return t

        for i in graph[nd]:
            if i not in vis and t + graph[nd][i] < total[i]:
                total[i] = t + graph[nd][i]
                heapq.heappush(hp, (total[i], i))


def main():
    sx, sy, ex, ey = map(int, input().split())
    nodes = [(sx, sy), (ex, ey)]
    graph = defaultdict(dict)

    while True:
        try:
            line = list(map(int, input().split()))
            for i in range(len(line) // 2 - 1):
                x, y = line[2 * i], line[2 * i + 1]
                nodes.append((x, y))
                if i:
                    px, py = line[2 * i - 2], line[2 * i - 1]
                    d = ((x - px) ** 2 + (y - py) ** 2) ** .5
                    graph[(x, y)][(px, py)] = graph[(px, py)][(x, y)] = d * 60 / 40000
        except EOFError:
            break

    for u in nodes:
        for v in nodes:
            if v not in graph[u] or u not in graph[v]:
                graph[u][v] = graph[v][u] = ((u[0] - v[0]) ** 2 + (u[1] - v[1]) ** 2) ** .5 * 60 / 10000

    t = min_time(len(nodes), graph, nodes)
    print(int(t) + (t % 1 >= 0.5))


if __name__ == '__main__':
    main()