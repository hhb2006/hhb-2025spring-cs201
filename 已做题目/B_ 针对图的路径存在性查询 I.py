class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        class UnionFind:
            def __init__(self, size):
                self.parent = list(range(size))
                self.rank = [1] * size
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


        uf = UnionFind(n)        
        for i in range(n):
            for j in range(i + 1, n):
                if abs(nums[i] - nums[j]) <= maxDiff:
                    uf.union(i, j)

        res = []
        for u, v in queries:
            res.append(uf.find(u) == uf.find(v))
        return res
