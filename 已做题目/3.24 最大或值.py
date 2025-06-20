class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        pre, suf, res = 0, [0], 0
        for i in range(len(nums)-1):
            suf.append(suf[-1] | nums[-i-1])
        for i in range(len(nums)):
            if i:
                pre |= nums[i-1]
            res = max(res, pre | suf[-i-1] | (nums[i] << k))
        return res

# https://leetcode.cn/problems/maximum-or/