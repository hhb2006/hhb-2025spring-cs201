class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank =  [1] * size

    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, a, b):
        r1 = self.find(a)
        r2 = self.find(b)
        if r1 != r2:
            if self.rank[r1] < self.rank[r2]:
                self.parent[r1] = r2
            else:
                self.parent[r2] = r1
                if self.rank[r1] == self.rank[r2]:
                    self.rank[r1] += 1


def main():
    n, k = map(int, input().split())
    uf = UnionFind(3 * n + 1)
    false_count = 0

    for _ in range(k):
        d, x, y = map(int, input().split())
        if x > n or y > n:
            false_count += 1
            continue
        if d == 1:
            if uf.find(x) == uf.find(y + n) or uf.find(x) == uf.find(y + 2 * n):
                false_count += 1
            else:
                uf.union(x, y)
                uf.union(x + n, y + n)
                uf.union(x + 2 * n, y + 2 * n)
        elif d == 2:
            if uf.find(x) == uf.find(y) or uf.find(x) == uf.find(y + 2 * n):
                false_count += 1
            else:
                uf.union(x, y + n)
                uf.union(x + n, y + 2 * n)
                uf.union(x + 2 * n, y)

    print(false_count)

if __name__ == "__main__":
    main()