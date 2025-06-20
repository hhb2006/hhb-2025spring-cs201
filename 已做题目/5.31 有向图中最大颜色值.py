class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        kinds = list(set(list(colors)))
        res = 1
        cnt = 0
        vals = {i: {j: 0 for j in kinds} for i in range(n)}
        graph = {i: [] for i in range(n)}
        in_deg = {i: 0 for i in range(n)}

        for u, v in edges:
            if u in graph[v]:
                return -1
            graph[u].append(v)
            in_deg[v] += 1

        q = deque([i for i in in_deg if in_deg[i] == 0])

        while q:
            u = q.popleft()
            vals[u][colors[u]] = max(1, vals[u][colors[u]])
            cnt += 1
            for v in graph[u]:
                in_deg[v] -= 1
                if in_deg[v] == 0:
                    q.append(v)
                for c in kinds:
                    if c == colors[v]:
                        vals[v][c] = max(vals[v][c], vals[u][c] + 1)
                    else:
                        vals[v][c] = max(vals[v][c], vals[u][c])
                    res = max(res, vals[v][c])

        if cnt != n:
            return -1

        return res