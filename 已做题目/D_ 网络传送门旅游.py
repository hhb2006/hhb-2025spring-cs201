class Solution:
    def minMoves(self, matrix: List[str]) -> int:
        if matrix[-1][-1] == '#':
            return -1

        m, n = len(matrix), len(matrix[0])
        q = deque([(0, 0)])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        doors = {chr(ord('A') + x): [] for x in range(26)}
        times = [[float('inf')] * n for _ in range(m)]
        times[0][0] = 0

        for i in range(m):
            for j in range(n):
                if 'A' <= matrix[i][j] <= 'Z':
                    doors[matrix[i][j]].append((i, j))

        while q:
            x, y = q.popleft()
            t = times[x][y]

            if x == m - 1 and y == n - 1:
                return t

            if 'A' <= matrix[x][y] <= 'Z' and doors[matrix[x][y]]:
                for nx, ny in doors[matrix[x][y]]:
                    if t < times[nx][ny]:
                        times[nx][ny] = t
                        q.appendleft((nx, ny))
                doors[matrix[x][y]].clear()

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] != '#' and t + 1 < times[nx][ny]:
                    times[nx][ny] = t + 1
                    q.append((nx, ny))

        return -1