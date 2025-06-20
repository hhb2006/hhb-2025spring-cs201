from collections import deque

def achieve(v1, v2, tg):
    dic = {1: 'FILL(1)', 2: 'FILL(2)', 3: 'POUR(1,2)',
           4: 'POUR(2,1)', 5: 'DROP(1)', 6: 'DROP(2)'}
    q = deque([(0, 0, 0, [])])    # potA, potB, step, path
    vis = {(0, 0)}
    while q:
        c1, c2, step, path = q.popleft()
        if c1 == tg or c2 == tg:
            return step, path
        for d1, d2, opr in [(v1, 0, 1), (0, v2, 2), (c2-v2, c1, 3),
                            (c2, c1-v1, 4), (-c1, 0, 5), (0, -c2, 6)]:
            n1 = min(c1+d1, v1) if d1 >= 0 else max(c1+d1, 0)
            n2 = min(c2+d2, v2) if d2 >= 0 else max(c2+d2, 0)
            op = dic[opr]
            if (n1, n2) not in vis:
                #print(n1,n2,step+1, path+[op])
                vis.add((n1, n2))
                q.append((n1, n2, step+1, path+[op]))
    return 'impossible', []


a,b,c = map(int, input().split())
cnt, way = achieve(a, b, c)
print(cnt)
for x in way:
    print(x)

# http://cs101.openjudge.cn/25dsapre/03151
# >>> 3 5 4
# FILL(2)
# POUR(2,1)
# DROP(1)
# POUR(2,1)
# FILL(2)
# POUR(2,1)/

'''
another version (given by DeepSeek) :
from collections import deque

def achieve(v1, v2, tg):
    # 检查目标是否可能达到
    if tg > max(v1, v2):
        return 'impossible', []

    dic = {1: 'FILL(1)', 2: 'FILL(2)', 3: 'POUR(1,2)',
           4: 'POUR(2,1)', 5: 'DROP(1)', 6: 'DROP(2)'}
    q = deque([(0, 0, 0, [])])  # potA, potB, step, path
    vis = {(0, 0)}
    max_steps = 10000  # 限制最大步数

    while q:
        c1, c2, step, path = q.popleft()
        if c1 == tg or c2 == tg:
            return step, path
        if step >= max_steps:
            return 'impossible', []
        for d1, d2, opr in [(v1, 0, 1), (0, v2, 2), (c2-v2, c1, 3),
                            (c2, c1-v1, 4), (-c1, 0, 5), (0, -c2, 6)]:
            n1 = min(c1+d1, v1) if d1 >= 0 else max(c1+d1, 0)
            n2 = min(c2+d2, v2) if d2 >= 0 else max(c2+d2, 0)
            op = dic.get(opr, 'UNKNOWN')
            if (n1, n2) not in vis:
                vis.add((n1, n2))
                q.append((n1, n2, step+1, path+[op]))
    return 'impossible', []

# 输入处理
try:
    a, b, c = map(int, input().split())
    cnt, way = achieve(a, b, c)
    print(cnt)
    for x in way:
        print(x)
except ValueError:
    print("Invalid input format. Please enter three integers.")
'''