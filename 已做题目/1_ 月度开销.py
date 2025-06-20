from typing import List

def arrange(lth: int, expense: List[int], t: int):
    l, r, res = max(expense), sum(expense), 0
    while l <= r:
        tg = (l + r) // 2

        p1, p2, exp, cnt = 0, 0, 0, 1
        while p2 < lth:
            if exp + expense[p2] > tg:
                exp = expense[p2]
                cnt += 1
            else:
                exp += expense[p2]
            p2 += 1
        # print(tg, cnt, l, r)
        if cnt > t:
            l = tg + 1
        else:
            res = tg
            r = tg - 1
    return res

n, m = map(int, input().split())
ep = [int(input()) for _ in range(n)]
print(arrange(n, ep, m))

# http://cs101.openjudge.cn/practice/04135