stk = list(map(str, input().split()))
res = []
while len(stk) > 1:
    res += stk[-2:]
    stk.pop()
    stk.pop()
res.append(stk[0])
res.reverse()
print(*res)

# https://sunnywhy.com/sfbj/7/1/296