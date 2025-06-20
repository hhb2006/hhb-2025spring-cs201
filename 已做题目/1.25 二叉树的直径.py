# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def height(rt):
            nonlocal res
            if not rt:
                return 0
            hl, hr = height(rt.left), height(rt.right)
            res = max(res, hl + hr)
            return max(hl, hr) + 1

        height(root)
        return res


# another format
class Solution1:
    def __init__(self):     # probably necessary
        self.res = None

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def height(rt):
            if not rt:
                return 0
            hl, hr = height(rt.left), height(rt.right)
            self.res = max(self.res, hl + hr)
            return max(hl, hr) + 1

        height(root)
        return self.res


# https://leetcode.cn/problems/diameter-of-binary-tree/