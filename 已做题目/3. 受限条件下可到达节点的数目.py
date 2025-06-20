from collections import deque


def most_reach(n, graph, re):
    q = deque([0])
    vis = set()
    cnt = 0

    while q:
        u = q.popleft()
        vis.add(u)
        cnt += 1
        for v in graph[u]:
            if v not in vis and v not in re:
                q.append(v)
    return cnt


def main():
    n = int(input())
    graph = {i: [] for i in range(n)}
    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    restricted = set(map(int, input().split()))
    print(most_reach(n, graph, restricted))


if __name__ == '__main__':
    main()