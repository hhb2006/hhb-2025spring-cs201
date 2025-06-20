from collections import deque


def bfs(m, n, mtx, b1, b2, e1, e2, orient):

    q = deque([(b1, b2, orient, 0)])
    vis = {(b1, b2, orient)}
    while q:
        x, y, ori, t = q.popleft()
        if x == e1 and y == e2:
            return t
        if (x, y, (ori[1], ori[0])) not in vis:
            q.append((x, y, (ori[1], ori[0]), t + 1))
            vis.add((x, y, (ori[1], ori[0])))
        if (x, y, (-ori[1], -ori[0])) not in vis:
            q.append((x, y, (-ori[1], -ori[0]), t + 1))
            vis.add((x, y, (-ori[1], -ori[0])))
        for step in range(1, 4):
            nx, ny = x + step * ori[0], y + step * ori[1]
            if nx in range(m - 1) and ny in range(n - 1) and mtx[nx][ny] != 1:
                if (nx, ny, ori) not in vis:
                    q.append((nx, ny, ori, t + 1))
                    vis.add((nx, ny, ori))
            else:
                break
    return -1



def main():
    dirs = {'east': (0, 1), 'south': (1, 0), 'west': (0, -1), 'north': (-1, 0)}
    while True:
        m, n = map(int, input().split())
        if m == n == 0:
            break
        field = [list(map(int, input().split())) for _ in range(m)]
        b1, b2, e1, e2, ori = map(str, input().split())
        b1, b2, e1, e2, ori = int(b1)-1, int(b2)-1, int(e1)-1, int(e2)-1, dirs[ori]
        rails = [[0] * (n - 1) for _ in range(m - 1)]
        for i in range(m):
            for j in range(n):
                if field[i][j]:
                    for di, dj in [(0, 0), (0, -1), (-1, 0), (-1, -1)]:
                        if i + di in range(m - 1) and j + dj in range(n - 1):
                            rails[i + di][j + dj] = 1
        field.clear()
        print(bfs(m, n, rails, b1, b2, e1, e2, ori))

if __name__ == '__main__':
    main()

# http://cs101.openjudge.cn/2025sp_routine/01376/