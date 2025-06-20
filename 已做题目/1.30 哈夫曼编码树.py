import sys

def build_huffman_tree(char_set: list):
    if len(char_set) == 1:
        return {char_set[0][0]: '0'}

    codes = {x[0]: '' for x in char_set}
    while len(char_set) > 1:
        l_node = char_set.pop()
        r_node = char_set.pop()
        l_char, r_char = l_node[0], r_node[0]
        new_char = []
        for char in l_char:
            codes[char] = '0' + codes[char]
            new_char.append(char)
        for char in r_char:
            codes[char] = '1' + codes[char]
            new_char.append(char)
        new_char.sort()
        new_char = ''.join(new_char)
        new_node = (new_char, l_node[1]+r_node[1])
        char_set.append(new_node)
        char_set.sort(key = lambda x: x[0], reverse = True)
        char_set.sort(key = lambda x: x[1], reverse = True)
    return codes


def encode(dic: dict, chars: str):
    res = ''
    for char in chars:
        if char != ' ':
            res += dic[char]
    return res


def decode(dic: dict, code: str):
    res = ''
    vals = dic.values()
    re_tree = {dic[x]: x for x in dic}
    l, r = 0, 1
    while r <= len(code):
        if code[l:r] in vals:
            res += re_tree[code[l:r]]
            l, r = r, r+1
        else:
            r += 1
    return res


n = int(input())
lis = []
for _ in range(n):
    a, b = map(str, input().split())
    b = float(b)
    lis.append((a,b))
lis.sort(key = lambda x: x[0], reverse = True)
lis.sort(key = lambda x: x[1], reverse = True)
huffman_tree = build_huffman_tree(lis)

lines = sys.stdin.read().splitlines()
for line in lines:
    if line[0] == '0' or line[0] == '1':
        print(decode(huffman_tree, line))
    else:
        print(encode(huffman_tree, line))

# http://cs101.openjudge.cn/practice/22161/