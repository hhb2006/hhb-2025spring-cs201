from collections import deque

def min_step(maze,s,e):
    sx,sy = s
    ex,ey = e
    q = deque([(sx, sy, 0)])    # (x, y, step)
    vis = {s}
    while q:
        x, y, step = q.popleft()
        if (x, y) == (ex, ey):
            return step
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and (nx, ny) not in vis:
                if maze[nx][ny] == '.':
                    q.append((nx, ny, step + 1))
                elif maze[nx][ny] == 'T':
                    return step + 1
                vis.add((nx, ny))
    return -1

n,m = map(int, input().split())
matrix = [list(input()) for _ in range(n)]
start = end = (0,0)
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 'S':
            start = (i, j)
        elif matrix[i][j] == 'T':
            end = (i, j)
print(min_step(matrix, start, end))

# https://sunnywhy.com/sfbj/8/2/323