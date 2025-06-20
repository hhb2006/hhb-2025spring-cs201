# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        node = root
        height = 0

        while node:
            node = node.left
            height += 1

        if height <= 1:
            return height

        def bisearch(nd, level):
            if level == 1:
                return 1
            rt = nd
            nd = nd.right
            for _ in range(level - 2):
                nd = nd.left
            if nd:
                return 2**(level - 2) + bisearch(rt.right, level - 1)
            return bisearch(rt.left, level - 1)

        return 2**(height - 1) - 1 + bisearch(root, height)