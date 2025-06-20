# Definition for singly-linked list.
#class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return
        if not list1:
            return list2
        if not list2:
            return list1

        cur1, cur2 = list1, list2
        root = ListNode()
        node = root

        while True:
            if not cur1:
                node.next = cur2
                break
            if not cur2:
                node.next = cur1
                break
            if cur1.val < cur2.val:
                node.next = cur1
                node = cur1
                cur1 = cur1.next
            else:
                node.next = cur2
                node = cur2
                cur2 = cur2.next

        return root.next

# https://leetcode.cn/problems/merge-two-sorted-lists/