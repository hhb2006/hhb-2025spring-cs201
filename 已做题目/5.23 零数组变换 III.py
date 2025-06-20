class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        diff = [nums[0]] + [nums[i + 1] - nums[i] for i in range(n - 1)]
        hp = []
        queries.sort()
        num, q = 0, 0

        for i in range(n):
            num += diff[i]
            while q < len(queries) and queries[q][0] <= i:
                heappush(hp, -queries[q][1])
                q += 1
            while num > 0 and hp and -hp[0] >= i:
                num -= 1
                r = -heappop(hp)
                if r < n - 1:
                    diff[r + 1] += 1
            if num > 0:
                return -1

        return len(hp)