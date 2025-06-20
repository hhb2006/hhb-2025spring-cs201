class UnionFind:
    def __init__(self, size = 0):
        self.parent = list(range(size))
        self.rank =  [1] * size           # 秩（树的高度）数组，用于按秩合并
        self.count = size                # 连通分量的数量

    def find(self, x):
        # 查找根节点，并进行路径压缩
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 递归路径压缩
        return self.parent[x]

    def union(self, x, y):
        # 合并两个节点的所在集合
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            # 按秩合并：将较矮的树合并到较高的树上
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                # 若两棵树高度相同，则合并后树的高度+1
                if self.rank[root_x] == self.rank[root_y]:
                    self.rank[root_x] += 1
            self.count -= 1  # 连通分量数量减1


def main():
    n, m = map(int, input().split())
    costs = list(map(int, input().split()))
    uf = UnionFind(n)
    roots = set()

    for _ in range(m):
        a, b = map(int ,input().split())
        uf.union(a - 1, b - 1)

    for i in range(n):
        p = uf.find(i)
        costs[p] = min(costs[p], costs[i])
        roots.add(p)

    print(sum(costs[r] for r in roots))


if __name__ == '__main__':
    main()