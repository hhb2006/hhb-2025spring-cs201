from typing import List


class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        n, m = len(grid), len(grid[0])
        elements, ans = [], 0

        for i in range(n):
            grid[i].sort(reverse = True)
            for j in range(limits[i]):
                elements.append((grid[i][j]))
        elements.sort(reverse = True)

        return sum(elements[0:k])

# 	https://leetcode.cn/problems/maximum-sum-with-at-most-k-elements/


