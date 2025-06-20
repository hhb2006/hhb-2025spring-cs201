class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


def height(node: TreeNode):
    if node is None:
        return -1
    return max(height(node.left) + 1, height(node.right) + 1)


def count_leaves(bi_tree):
    res = 0
    for node in bi_tree:
        if not node.left and not node.right:
            res += 1
    return res


n = int(input())  # the number of nodes
is_child = [False for _ in range(n)]
tree = [TreeNode(_) for _ in range(n)]
for i in range(n):
    l, r = map(int, input().split())
    if l == -1:
        tree[i].left = None
    else:
        is_child[l] = True
        tree[i].left = tree[l]
    if r == -1:
        tree[i].right = None
    else:
        is_child[r] = True
        tree[i].right = tree[r]

root = tree[0]
for i in range(n):
    if not is_child[i]:
        root = tree[i]
        break

h = height(root)
cnt = count_leaves(tree)
print(h, cnt)

# http://cs101.openjudge.cn/25dsapre/27638/