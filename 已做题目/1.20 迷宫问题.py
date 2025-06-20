from collections import deque

def min_step(maze):
    q = deque([(0, 0, 0)])    # (x, y, step)
    vis = [(0, 0)]
    while q:
        x, y, step = q.popleft()
        if (x, y) == (len(maze)-1, len(maze[0])-1):
            return step
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and (nx, ny) not in vis:
                if maze[nx][ny] == 0:
                    q.append((nx, ny, step + 1))
                vis.append((nx, ny))
    return -1

n,m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
print(min_step(matrix))

# https://sunnywhy.com/sfbj/8/2/320