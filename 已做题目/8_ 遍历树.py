class TreeNode:
    def __init__(self, val = 0, kids = None):
        if kids is None:
            kids = []
        self.val = val
        self.kids = kids

def traversal(root):
    if not root:
        return
    nodes = [root] + root.kids
    nodes.sort(key = lambda x: x.val)
    for node in nodes:
        if node == root:
            print(root.val)
        else:
            traversal(node)
    return


n = int(input())
vis, not_root, rt = dict(), set(), None

for _ in range(n):
    nums = list(map(int, input().split()))
    for i in range(len(nums)):
        if nums[i] in vis:
            nums[i] = vis[nums[i]]
        else:
            j = nums[i]
            nums[i] = TreeNode(nums[i])
            vis[j] = nums[i]
        if i:
            not_root.add(nums[i])
    nums[0].kids = nums[1:]

for nd in vis.values():
    if nd not in not_root:
        rt = nd

traversal(rt)



# http://cs101.openjudge.cn/practice/27928/