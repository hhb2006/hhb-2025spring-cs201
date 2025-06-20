# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')

        def path_sum(node):
            nonlocal res

            if not node:
                return 0

            l, r = path_sum(node.left), path_sum(node.right)
            res = max(max(l, r, l + r, 0) + node.val, res)
            return max(l, r, 0) + node.val

        path_sum(root)
        return int(res)