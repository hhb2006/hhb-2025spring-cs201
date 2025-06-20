from typing import List


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        dic = dict()
        for i in range(n):
            d = nums[i] - i
            if d not in dic.keys():
                dic[d] = 1
            else:
                dic[d] += 1
        return (n ** 2 - n - sum(dic[i] ** 2 - dic[i] for i in dic.keys())) // 2

# https://leetcode.cn/problems/count-number-of-bad-pairs/