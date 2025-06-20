from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def arrange(i):
            nonlocal nums
            if i == 0:
                return [[nums[i]]]
            else:
                arrange(i-1)
                total = [lis[:j]+[nums[i]]+lis[j:] for j in range(i+1) for lis in arrange(i-1)]
            return total

        a = arrange(len(nums) - 1)
        return sorted(a)


if __name__ == '__main__':
    print(Solution().permute([1, 2, 3]))