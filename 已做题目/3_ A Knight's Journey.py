dirs = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def journey(path, x, y, vis):
    move, res = 0, ''
    if len(path) == p * q * 2:
        return path
    next_step = sorted([(y + dy, x + dx) for (dx, dy) in dirs])
    for ny, nx in next_step:
        if nx in range(p) and ny in range(q):
            if (nx, ny) not in vis:
                move = 1
                vis.append((nx, ny))
                res = journey(path + f'{letters[ny]}{nx + 1}', nx, ny, vis)
                if res:
                    return res
                vis.pop()
    if not move:
        return ''


def find_way(a, b):
    for i in range(a):
        for j in range(b):
            visited = [(i, j)]
            paths = journey(f'{letters[i]}{j + 1}', i, j, visited)
            if paths:
                return paths
    return 'impossible'


n = int(input())
for _ in range(n):
    p, q = map(int, input().split())
    print(f'Scenario #{_ + 1}:')
    print(find_way(p, q))
    if _ != n-1:
        print()