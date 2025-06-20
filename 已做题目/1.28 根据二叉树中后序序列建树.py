def build_tree(inorder, postorder):
    n = len(inorder)
    if not n:
        return ''
    node = postorder[-1]
    i = 0
    while inorder[i] != node:
        i += 1
    return (node + build_tree(inorder[0:i], postorder[0:i])
            + build_tree(inorder[i+1:], postorder[i:n-1]))

print(build_tree(input(), input()))

# http://cs101.openjudge.cn/practice/24750/