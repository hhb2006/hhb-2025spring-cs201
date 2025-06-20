class BiTreeNode:
    def __init__(self, val='', left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def in_order_traversal(node: BiTreeNode):
    if not node:
        return []
    return (in_order_traversal(node.left) + [node.val]
            + in_order_traversal(node.right))


def post_order_traversal(node: BiTreeNode):
    if not node:
        return []
    return (post_order_traversal(node.left) +
            post_order_traversal(node.right) + [node.val])


def build_tree_by_dots(s: str):
    if not s:
        return None
    root = BiTreeNode(s[0])
    nodeStack = [root]
    for i in range(1, len(s)):
        nodeStack.append(BiTreeNode(s[i]))
        if nodeStack[-2].left:
            nodeStack[-2].right = nodeStack[-1]
        else:
            nodeStack[-2].left = nodeStack[-1]

        if nodeStack[-1].val == '.':
            nodeStack.pop()
        while nodeStack and nodeStack[-1].left and nodeStack[-1].right:
                nodeStack.pop()

    return root


rt = build_tree_by_dots(input())
mid = in_order_traversal(rt)
post = post_order_traversal(rt)
for a in mid:
    if a != '.':
        print(a, end='')
print()
for b in post:
    if b != '.':
        print(b, end='')

# http://cs101.openjudge.cn/25dsapre/08581/