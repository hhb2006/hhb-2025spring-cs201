n = int(input())
stack = []
for _ in range(n):
    s = input()
    if s == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    else:
        num = int(s.split()[1])
        stack.append(num)