from collections import deque


class BiTreeNode:
    def __init__(self, val = '', left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return self.val


def pre_order_traversal(node):
    if node:
        return ([node.val] + pre_order_traversal(node.left)
                + pre_order_traversal(node.right))
    return []


def post_order_traversal(node):
    if node:
        return (post_order_traversal(node.left)
                + post_order_traversal(node.right) + [node.val])
    return []


def in_order_traversal(node):
    if node:
        return (in_order_traversal(node.left) + [node.val]
                + in_order_traversal(node.right))
    return []


def build_tree(nodes):
    rt = nodes[0][0]
    q = deque([])
    while nodes:
        node, level = nodes.pop()
        if node.val == '*':
            node = None
        if q and q[0][1] == level + 1:
            node.left = q[0][0]
            q.popleft()
        if q and q[0][1] == level + 1:
            node.right = q[0][0]
            q.popleft()
        q.appendleft((node, level))
    return rt


def main():
    n = int(input())
    for _ in range(n):
        lis = []
        while True:
            inp = input()
            if inp == '0':
                break
            lis.append((BiTreeNode(inp[-1]), len(inp)))
        root = build_tree(lis.copy())
        print(''.join(pre_order_traversal(root)))
        print(''.join(post_order_traversal(root)))
        print(''.join(in_order_traversal(root)))
        print()


if __name__ == '__main__':
    main()


# http://cs101.openjudge.cn/2025sp_routine/03720/