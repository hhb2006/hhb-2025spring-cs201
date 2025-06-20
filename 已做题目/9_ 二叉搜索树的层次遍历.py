from collections import deque


class BiTreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


def level_order_traversal(root):
    res = []
    if not root:
        return res
    q = deque([root])
    while q:
        node = q.popleft()
        res.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return res


def insert(root, node):
    if node.val > root.val:
        if not root.right:
            root.right = node
        else:
            insert(root.right, node)
    else:
        if not root.left:
            root.left = node
        else:
            insert(root.left, node)
    return


def build_tree(nodes):
    root = nodes[0]
    if len(nodes) == 1:
        return root
    for node in nodes[1:]:
        if node:
            insert(root, node)
    return root


def main():
    lis = list((map(int, input().split())))
    vis = set()
    for i in range(len(lis)):
        if lis[i] in vis:
            lis[i] = None
            continue
        vis.add(lis[i])
        lis[i] = BiTreeNode(lis[i])
    root = build_tree(lis)
    print(*level_order_traversal(root), end = '')


if __name__ == '__main__':
    main()