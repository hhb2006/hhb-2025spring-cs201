class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [nums[0]] + [nums[i + 1] - nums[i] for i in range(n - 1)]
        for l, r in queries:
            diff[l] -= 1
            if r < n - 1:
                diff[r + 1] += 1

        num = 0
        for i in range(n):
            num += diff[i]
            if num > 0:
                return False
        return True

# https://leetcode.cn/problems/zero-array-transformation-i/