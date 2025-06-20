import sys

def build_tree(preorder: str, inorder: str) -> str:
    n = len(preorder)
    if n == 0:
        return ''
    node = preorder[0]
    i = 0
    while node != inorder[i]:
        i += 1
    return (build_tree(preorder[1:i+1], inorder[:i]) +
            build_tree(preorder[i+1:], inorder[i+1:]) + node)

lines = sys.stdin.read().splitlines()
inp, t = [], 0
for line in lines:
    if line:
        t += 1
        inp.append(line)
    else:
        break
for j in range(t//2):
    print(build_tree(inp[2*j], inp[2*j+1]))

# http://cs101.openjudge.cn/practice/22158/