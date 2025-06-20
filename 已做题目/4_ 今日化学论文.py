def decode(s):
    n = len(s)
    char, pos = [], []
    p = 0
    for i in range(n-1, -1, -1):
        if s[i] == ']':
            pos.append(p)
        elif s[i] == '[':
            pre = pos.pop()
            times, st = '', ''
            for j in range(pre, p):
                c = char.pop()
                if '0' <= c <= '9':
                    times += c
                else:
                    st += c
            st = st * int(times)
            char.append(st)
            p = pre + 1
        else:
            char.append(s[i])
            p += 1
    char.reverse()
    return ''.join(char)


print(decode(input()))