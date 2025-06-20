# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        if not head.next:
            return head

        pre = head
        cur = head.next
        pre.next = None

        while cur.next:
            new = cur.next
            cur.next = pre
            pre, cur = cur, new

        cur.next = pre
        return cur