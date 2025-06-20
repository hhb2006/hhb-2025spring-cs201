from collections import deque


t = int(input())
teams = dict()

for i in range(t):
    teammates = input().split()
    for teammate in teammates:
        teams[teammate] = i

q = deque()
sign = deque()

while True:
    opr = input()
    if opr == 'STOP':
        break
    elif opr == 'DEQUEUE':
        tm = q.popleft()
        mt = tm.popleft()
        print(mt)
        if tm:
            q.appendleft(tm)
        else:
            sign.popleft()
    else:
        mate = opr.split()[-1]
        if mate in teams:
            team = teams[mate]
            for i in range(len(sign)):
                if sign[i] == team:
                    q[i].append(mate)
                    break
            else:
                sign.append(team)
                q.append(deque([mate]))
        else:
            teams[mate] = len(sign)
            sign.append(len(sign))
            q.append(deque([mate]))


# http://cs101.openjudge.cn/practice/27925/