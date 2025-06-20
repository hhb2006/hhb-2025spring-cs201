from typing import List


class SolutionDfs:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        from functools import lru_cache


        @lru_cache(maxsize = None)
        def dfs(n, d, lis):
            if n == len(lis):
                return [[]]
            res = [[lis[n]]]
            for i in range(n + 1, len(lis)):
                if lis[i] - lis[n] < d:
                    remain = dfs(i, d, lis)
                    for subset in remain:
                        if lis[n] + d not in subset:
                            res.append([lis[n]] + subset)
                if lis[i] - lis[n] > d:
                    remain = dfs(i, d, lis)
                    for subset in remain:
                        res.append([lis[n]] + subset)
            return res

        cnt = 0
        nums.sort()
        nums = tuple(nums)
        for j in range(len(nums)):
            cnt += len(dfs(j, k, nums))
        return cnt

if __name__ == '__main__':
    print(SolutionDfs().beautifulSubsets([10,4,5,7,2,1], 3))


class SolutionDp:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        groups = defaultdict(dict)
        for a in nums:
            mod = a % k
            groups[mod][a] = groups[mod].get(a, 0) + 1
        ans = 1
        for g in groups.values():
            sorted_keys = sorted(g.keys())
            m = len(sorted_keys)
            f = [[0] * 2 for _ in range(m)]
            f[0][0] = 1
            f[0][1] = (1 << g[sorted_keys[0]]) - 1
            for i in range(1, m):
                f[i][0] = f[i - 1][0] + f[i - 1][1]
                if sorted_keys[i] - sorted_keys[i - 1] == k:
                    f[i][1] = f[i - 1][0] * ((1 << g[sorted_keys[i]]) - 1)
                else:
                    f[i][1] = (f[i - 1][0] + f[i - 1][1]) * ((1 << g[sorted_keys[i]]) - 1)
            ans *= f[m - 1][0] + f[m - 1][1]
        return ans - 1
