# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def cnt(node, tgs):
            if not node:
                return 0
            value = node.val
            res = 1 if value == targetSum else 0
            for i in range(tgs):
                if tgs[i] == value:
                    res += 1
                tgs[i] -= value
            res += cnt(node.left, tgt) + cnt(node.right, tgt)
            return res

        return cnt(root, [])