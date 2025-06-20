# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [(root, 1)]
        res = 1
        while stack:
            root, depth = stack.pop()
            l, r = root.left, root.right
            if l or r:
                if l:
                    stack.append((l, depth + 1))
                if r:
                    stack.append((r, depth + 1))
            else:
                res = max(res, depth)
        return res

# https://leetcode.cn/problems/maximum-depth-of-binary-tree/