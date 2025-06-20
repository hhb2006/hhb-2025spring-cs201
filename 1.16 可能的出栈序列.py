def is_legal(given_lth: int, given_seq: list):
    nums = [_ for _ in range(0, given_lth + 1)]
    stk = []
    flag = True
    mx = 0
    for i in range(given_lth):
        if given_seq[i] >= mx:
            stk += nums[mx + 1:given_seq[i]]
            mx = given_seq[i]
        else:
            if stk.pop() != given_seq[i]:
                flag = False
                break
    return flag

def dfs(m, seq, used):
    if len(seq) == m:
        if is_legal(m, seq):
            print(*seq)
        return
    for i in range(1, m + 1):
        if not used[i]:
            seq.append(i)
            used[i] = 1
            dfs(m, seq, used)
            seq.pop()
            used[i] = 0

n = int(input())
dfs(n, [], [0 for _ in range(n + 1)])