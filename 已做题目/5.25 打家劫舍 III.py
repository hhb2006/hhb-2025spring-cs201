# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @lru_cache(maxsize = None)
        def dfs(node, stolen):
            if not node:
                return 0
            if stolen:
                return dfs(node.left, 0) + dfs(node.right, 0) + node.val
            return max(dfs(node.left, 0), dfs(node.left, 1)) + max(dfs(node.right, 0), dfs(node.right, 1))

        return max(dfs(root, 0), dfs(root, 1))

