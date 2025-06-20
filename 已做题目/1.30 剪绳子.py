from bisect import bisect

n = int(input())
lth = list(map(int, input().split()))
lth.sort()
cost = 0

while len(lth) > 1:
    a = lth.pop(0)
    b = lth.pop(0)
    #print(a,b)
    cost += a+b
    ind = bisect(lth, a+b)
    if ind == len(lth):
        lth.append(a+b)
    else:
        lth.insert(ind, a+b)

print(cost)

# http://cs101.openjudge.cn/25dsapre/18164/