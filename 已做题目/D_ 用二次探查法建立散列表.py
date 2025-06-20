import sys
inp = sys.stdin.read
data = inp().split()
index = 0
n = int(data[index])
index += 1
m = int(data[index])
index += 1
num_list = [int(i) for i in data[index:index+n]]

vis = set()
vals = set()
dic = dict()
for num in num_list:
    if num in vals:
        continue
    key = num % m
    k = key
    r, s, t = 0, 1, 0
    while k in vis:
        if t % 2 == 0:
            r += 1
        k = (key + s * r ** 2) % m
        t += 1
        s *= -1
    dic[num] = k
    vis.add(k)
    vals.add(num)

res = [dic[x] for x in num_list]
print(*res)