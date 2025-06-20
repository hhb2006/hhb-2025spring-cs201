# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def routes(rt) -> list:
            if not rt:
                return []
            lis = routes(rt.left) + routes(rt.right)
            if not lis:
                return [str(rt.val)]
            for i in range(len(lis)):
                lis[i] = str(rt.val) + lis[i]
            return lis

        nums = routes(root)
        res = 0
        for num in nums:
            res += int(num)
        return res

# https://leetcode.cn/problems/sum-root-to-leaf-numbers/