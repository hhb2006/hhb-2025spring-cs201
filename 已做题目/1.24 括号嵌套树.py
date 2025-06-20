class TreeNode:
    def __init__(self, val='', children = None):
        if children is None:
            children = []
        self.val = val
        self.children = children


def pre_order_traversal(node: TreeNode):
    if not node:
        return []
    res = []
    for child in node.children:
        res += pre_order_traversal(child)
    return [node.val] + res


def post_order_traversal(node: TreeNode):
    if not node:
        return []
    res = []
    for child in node.children:
        res += post_order_traversal(child)
    return res + [node.val]


def build_tree_by_bracket(s: str):
    if not s:
        return None
    if len(s) == 1:
        return TreeNode(s[0])
    nodeStack = []
    bracketStack = []
    nodes = []
    for i, c in enumerate(s):
        #print(bracketStack, nodeStack)
        if 'A' <= c <= 'Z':
            c = TreeNode(c)
            nodes.append(c)
            if nodeStack:
                nodeStack[-1].children.append(c)
            if s[i+1] == '(':
                nodeStack.append(c)
        elif c == '(' :
            bracketStack.append(c)
        elif c == ')':
            bracketStack.pop()
            nodeStack.pop()
    return nodes[0]


rt = build_tree_by_bracket(input())
pre = pre_order_traversal(rt)
post = post_order_traversal(rt)
print(''.join(pre))
print(''.join(post))

# http://cs101.openjudge.cn/practice/24729/