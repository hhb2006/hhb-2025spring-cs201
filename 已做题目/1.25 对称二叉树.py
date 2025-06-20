# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# primitive method

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        cur_layer = [root]
        next_layer = []
        while True:
            while cur_layer:
                node = cur_layer.pop()
                if node:
                    next_layer.append(node.left)
                    next_layer.append(node.right)
            if not next_layer:
                break
            n = len(next_layer)
            for i in range(n):
                if next_layer[i] or next_layer[-i-1]:
                    if not next_layer[i] or not next_layer[-i-1]:
                        return False
                    if next_layer[i].val != next_layer[-i-1].val:
                        return False
            cur_layer, next_layer = next_layer, []
        return True


# improved method

class Solution1:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def recur(L, R):
            if not L and not R: return True
            if not L or not R or L.val != R.val: return False
            return recur(L.left, R.right) and recur(L.right, R.left)

        return not root or recur(root.left, root.right)



# https://leetcode.cn/problems/symmetric-tree/