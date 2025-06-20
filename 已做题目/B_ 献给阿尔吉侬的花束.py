from collections import deque


def min_time(s, e, maze):
    q = deque([(s[0], s[1], 0)])
    time, r, c = 0, len(maze), len(maze[0])
    vis = [[0] * c for _ in range(r)]
    while q:
        x, y, time = q.popleft()
        if (x, y) == e:
            return time
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c and (not vis[nx][ny]) and maze[nx][ny] != '#':
                q.append((nx, ny, time + 1))
                vis[nx][ny] = 1
    return 'oop!'


def main():
    t = int(input())
    for _ in range(t):
        r, c = map(int, input().split())
        maze = [input() for _ in range(r)]
        s, e = (0, 0), (0, 0)
        for i in range(r):
            for j in range(c):
                if maze[i][j] == 'S':
                    s = (i, j)
                elif maze[i][j] == 'E':
                    e = (i, j)
        print(min_time(s, e, maze))


if __name__ == '__main__':
    main()