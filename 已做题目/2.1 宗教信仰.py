class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank =  [1] * size
        self.count = size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                if self.rank[root_x] == self.rank[root_y]:
                    self.rank[root_x] += 1
            self.count -= 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def __repr__(self):
        return f"Parent: {self.parent}\nRank: {self.rank}\nCount: {self.count}"


t = 0
while True:
    t += 1
    N, M = map(int, input().split())
    if N == M == 0:
        exit()

    ds = UnionFind(N)
    for _ in range(M):
        a, b = map(int, input().split())
        ds.union(a-1, b-1)

    res = ds.count
    #print(ds)
    print(f'Case {t}: {res}')