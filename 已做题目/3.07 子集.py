class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(n, lis):
            if n == len(lis):
                return [[]]
            res = []
            remain = dfs(n + 1, lis)
            for subset in remain:
                res.append(subset)
                res.append([lis[n]] + subset)
            return res

        return dfs(0, nums)