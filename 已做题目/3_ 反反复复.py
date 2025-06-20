def decode(c, s):
    res = ''
    r = len(s) // c
    for i in range(c):
        for j in range(r):
            if j % 2:
                res += (s[(j + 1) * c - i - 1])
            else:
                res += (s[j * c + i])
    print(res)
    return


n = int(input())
string = input()
decode(n, string)