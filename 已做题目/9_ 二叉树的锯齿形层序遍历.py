# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res

        q = deque([root])
        odd = 0
        while q:
            odd = 1 - odd
            stk = []
            while q:
                stk.append(q.popleft())
            if odd:
                res.append([nd.val for nd in stk])
            else:
                res.append([nd.val for nd in stk[::-1]])
            for node in stk:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res