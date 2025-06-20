n = int(input())
seq = list(map(int, input().split()))
nums = [_ for _ in range(0,n+1)]
stk = []
flag = True
mx = 0
for i in range(n):
    if seq[i] >= mx:
        stk += nums[mx+1:seq[i]]
        mx = seq[i]
    else:
        if stk.pop() != seq[i]:
            flag = False
            break
    #print(stk)
print('Yes' if flag else 'No')

