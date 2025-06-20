def build_lps(patt):
    m = len(patt)
    lps = [0] * m
    i, j = 1, 0

    while i in range(m):
        if patt[i] == patt[j]:
            lps[i] = j + 1
            i += 1
            j += 1
        elif j == 0:
            i += 1
        else:
            j = lps[j - 1]
    return lps


def main():
    t = 0
    while True:
        t += 1
        n = int(input())
        if not n:
            break
        print(f'Test case #{t}')
        s = input()
        lps = build_lps(s)

        for i in range(1, n):
            if lps[i] and lps[i] % (i + 1 - lps[i]) == 0:
                print(i + 1, (i + 1) // (i + 1 - lps[i]))

        print()


if __name__ == '__main__':
    main()
