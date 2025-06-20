"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        q = deque([(root, 0)])
        cur_level = 0
        last = None
        while q:
            node, level = q.popleft()
            if level > cur_level:
                last = None
                cur_level = level
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
            if last:
                last.next = node
            last = node
        return root


class Solution1:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        start = root
        while start:
            self.last = None
            self.nextStart = None
            p = start
            while p:
                if p.left:
                    self.handle(p.left)
                if p.right:
                    self.handle(p.right)
                p = p.next
            start = self.nextStart
        return root

    def handle(self, p):
        if self.last:
            self.last.next = p
        if not self.nextStart:
            self.nextStart = p
        self.last = p


# https://leetcode.cn/problems/populating-next-right-pointers-in-each-node-ii/description/