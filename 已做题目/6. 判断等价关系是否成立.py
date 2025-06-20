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


def is_feasible(n, same, diff):
    uf = UnionFind(n)

    for a, b in same:
        if a == b:
            continue
        uf.union(a, b)

    for a, b in diff:
        r1, r2 = uf.find(a), uf.find(b)
        if r1 == r2:
            return False
    return True


def main():
    n = int(input())
    same, diff = [], []
    vis = set()
    dic = {}
    cnt = 0

    for _ in range(n):
        s = input()

        a, b = s[0], s[-1]
        if a not in vis:
            vis.add(a)
            dic[a] = cnt
            cnt += 1
        if b not in vis:
            vis.add(b)
            dic[b] = cnt
            cnt += 1

        if s[1] == '=':
            same.append((dic[a], dic[b]))
        elif s[1] == '!':
            diff.append((dic[a], dic[b]))

    res = is_feasible(cnt, same, diff)
    if res:
        print('True')
    else:
        print('False')


if __name__ == '__main__':
    main()