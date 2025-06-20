# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def build_tree(lis):
            if not lis:
                return None
            mid = len(lis) // 2
            root = lis[mid]
            root.left = build_tree(lis[:mid])
            root.right = build_tree(lis[mid + 1:])
            return root

        nodes = [TreeNode(nums[i]) for i in range(len(nums))]
        rt = build_tree(nodes)
        return rt

# https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/