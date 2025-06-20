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
    while True:
        n, m = map(int, input().split())
        if n == m == 0:
            return

        uf = UnionFind(n)
        suspects = 0
        for _ in range(m):
            group = list(map(int, input().split()))
            k = group[0]
            for i in range(2, k+1):
                uf.union(group[1], group[i])

        root = uf.find(0)
        for i in range(n):
            if uf.find(i) == root:
                suspects += 1
        print(suspects)


if __name__ == '__main__':
    main()