def feasible(lth, lines, k):
    cnt = 0
    for line in lines:
        cnt += line // lth
    if cnt >= k:
        return True
    return False


def main():
    N, K = map(int, input().split())
    cables = [100 * float(input()) for _ in range(N)]
    l, r, res = 1, max(cables), 0

    while l <= r:
        mid = (l + r) // 2
        if feasible(mid, cables, K):
            res = max(res, mid)
            l = mid + 1
        else:
            r = mid - 1

    print('%.2f'% (res / 100))


if __name__ == '__main__':
    main()