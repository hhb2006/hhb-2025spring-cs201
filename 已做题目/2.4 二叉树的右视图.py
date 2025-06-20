# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        from collections import deque

        def level_order_traversal(node):
            res = []
            if node:
                queue = deque([(0, node)])
                while queue:
                    level, node = queue.popleft()
                    res.append((level, node.val))
                    if node.left:
                        queue.append((level + 1, node.left))
                    if node.right:
                        queue.append((level + 1, node.right))
            return res


        levels = level_order_traversal(root)
        stack, right_view = [], []

        for i in range(len(levels)):
            if not stack:
                stack.append(levels[i])
            elif levels[i][0] != stack[-1][0]:
                right_view.append(stack.pop()[1])
                stack.clear()
                stack.append(levels[i])
            else:
                stack.append(levels[i])

        if stack:
            right_view.append(stack[-1][1])

        return right_view

# https://leetcode.cn/problems/binary-tree-right-side-view/