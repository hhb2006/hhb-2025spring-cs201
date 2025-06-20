def main():
    n = int(input())
    t = 1
    stack = []
    cnt = 0
    for _ in range(2 * n):
        request = input()
        if request[0] == 'a':
            num = int(request.split()[1])
            stack.append(num)
        elif request[0] == 'r':
            if stack[-1] != t:
                cnt += 1
                stack.sort(reverse = True)
            stack.pop()
            t += 1
    print(cnt)


if __name__ == '__main__':
    main()
