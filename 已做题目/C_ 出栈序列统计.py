n = int(input())
dp = [[0] * (n + 1) for _ in range(n + 1)]
dp[1][0] = 1
for push in range(1, n + 1):
    dp[push][0] = 1
    for pop in range(1, push + 1):
        if push == pop:
            dp[push][push] = dp[push][push - 1]
        else:
            dp[push][pop] = dp[push - 1][pop] + dp[push][pop - 1]
print(dp[-1][-1])