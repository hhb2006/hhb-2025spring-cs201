class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        airlines = {i: dict() for i in range(n)}
        possible = 0
        for a, b, c in flights:
            if b == dst:
                possible = 1
            airlines[a][b] = c

        if not possible:
            return -1

        def dijkstra(graph, lmt, s, e):
            hp = [(0, s, 0, 1)]

            while hp:
                total, u, edge, order= heapq.heappop(hp)
                if u == e and order <= lmt:
                    return total

                for v in graph[u]:
                    if order + 1 <= lmt:
                        cost = graph[u][v]
                        heapq.heappush(hp, (total + cost, v, cost, order + 1))
            return -1

        return dijkstra(airlines, k + 2, src, dst)