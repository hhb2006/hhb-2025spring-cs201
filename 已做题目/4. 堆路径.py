from collections import deque


class Node:
    def __init__(self, val = '0', left = None, right = None):
        self.val = int(val)
        self.left = left
        self. right = right
        self.route = [val]

    def compare(self, a):
        if self.val > a.val:
            return 1
        if self.val < a.val:
            return -1
        return 0


def all_route(root: Node):
    comp = set()
    routes = []
    kind = 'Not Heap'
    q = deque([root])

    while q:
        node = q.popleft()
        r, l = node.right, node.left
        if r:
            r.route += node.route
            q.append(r)
            comp.add(node.compare(r))
        if l:
            l.route += node.route
            q.append(l)
            comp.add(node.compare(l))
        if not (l or r):
            routes.append(node.route[::-1])

    if 1 not in comp:
        kind = 'Min Heap'
    elif -1 not in comp:
        kind = 'Max Heap'

    return routes, kind


def main():
    n = int(input())
    level_order = list(map(Node, input().split()))
    root = level_order[0]

    for i in range(n):
        if 2 * i + 1 < n:
            level_order[i].left = level_order[2 * i + 1]
        if 2 * i + 2 < n:
            level_order[i].right = level_order[2 * i + 2]

    routes, kind = all_route(root)
    for r in routes:
        print(*r)
    print(kind)


if __name__ == '__main__':
    main()