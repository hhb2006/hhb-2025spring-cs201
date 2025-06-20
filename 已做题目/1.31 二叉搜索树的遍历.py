class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)


def build_tree(n: int, preorder: list):
    if n == 0:
        return

    stk = [preorder[0]]
    for i in range(1, n):
        node = preorder[i]
        if node.val > stk[-1].val:
            pre = stk.pop()
            while stk:
                if node.val > stk[-1].val:
                    pre = stk.pop()
                else:
                    break
            pre.right = node
        else:
            stk[-1].left = node
        stk.append(node)



def pre_search(rt: Node):
    if not rt:
        return []
    return pre_search(rt.left) + pre_search(rt.right) + [rt.val]


def main():
    N = int(input())
    inp = list(map(int, input().split()))
    pre_order = [Node(x) for x in inp]
    build_tree(N, pre_order)
    print(*pre_search(pre_order[0]))

if __name__ == '__main__':
    main()