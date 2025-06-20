from collections import deque


n, m = map(int, input().split())
kids = list(map(int, input().split()))
q = deque([(i, kid) for i, kid in enumerate(kids)])
j = 0

while q:
    j, k = q.popleft()
    if k > m:
        q.append((j, k - m))

print(j + 1)