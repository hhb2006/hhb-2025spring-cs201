def longest_common_subsequence(a, b):
    prev = [0] * (len(b) + 1)
    curr = [0] * (len(b) + 1)
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i-1] == b[j-1]:
                curr[j] = max(prev[j-1] + 1, prev[j], curr[j-1])
            else:
                curr[j] = max(prev[j], curr[j-1])
        prev, curr = curr.copy(), [0] * (len(b) + 1)
    return prev[-1]


def cnt_insert(lth, s):
    return lth - longest_common_subsequence(s, s[::-1])

def main():
    n = int(input())
    print(cnt_insert(n, input()))

if __name__ == '__main__':
    main()


# http://cs101.openjudge.cn/2025sp_routine/01159/)