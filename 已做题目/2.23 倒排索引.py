from collections import defaultdict

n = int(input())
table = defaultdict(list)
for i in range(1, n + 1):
    lis = list(map(str, input().split()))
    for t in range(1, int(lis[0]) + 1):
        word = lis[t]
        if not table[word]:
            table[word].append(str(i))
        elif table[word][-1] != str(i):
            table[word].append(str(i))

m = int(input())
for _ in range(m):
    wd = input()
    if table[wd]:
        print(' '.join(table[wd]))
    else:
        print('NOT FOUND')

# http://cs101.openjudge.cn/2025sp_routine/06640/