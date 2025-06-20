def query(bit,lis):
    cnt = 0
    for num in lis:
        num = bin(num)
        num = num.replace('0b', '')
        if len(num) > bit:
            if str(num)[-bit-1] == '1':
                cnt += 1
    return cnt

n,m = map(int, input().split())
nums = list(map(int, input().split()))
for _ in range(m):
    op = input().split()
    if op[0] == 'Q':
        print(query(int(op[1]), nums))
    elif op[0] == 'C':
        nums = [(x+int(op[1]))%65535 for x in nums]

"""
in:
3 5
1 2 4
Q 1
Q 2
C 1
Q 1
Q 2
--
001
010
100

010
011
101

bit:
210

out:
1
1
2
1
--
"""
