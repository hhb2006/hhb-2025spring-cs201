class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        class UnionFind:
            def __init__(self, size):
                self.parent = list(range(size))  # 父节点数组，初始时每个节点的父节点是自己
                self.rank = [1] * size  # 秩（树的高度）数组，用于按秩合并
                self.count = size  # 连通分量的数量

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

            def __repr__(self):
                return f"Parent: {self.parent}\nRank: {self.rank}\nCount: {self.count}"


        n = len(grid)
        uf = UnionFind(n ** 2)
        blanks = set()
        areas = dict()
        max_area = 0

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    blanks.add((i, j))
                    continue
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                        uf.union(i * n + j, nx * n + ny)

        for i in range(n ** 2):
            p = uf.find(uf.parent[i])
            uf.parent[i] = p
            if p not in areas.keys():
                areas[p] = 1
            else:
                areas[p] += 1
            max_area = max(max_area, areas[p])

        for i, j in blanks:
            tags = set()
            s = 1
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = i + dx, j + dy
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1 and uf.parent[nx * n + ny] not in tags:
                    s += areas[uf.parent[nx * n + ny]]
                    tags.add(uf.parent[nx * n + ny])
            max_area = max(max_area, s)

        return max_area

# https://leetcode.cn/problems/making-a-large-island/
# 此题并查集不如直接用dfs