def main():
    n, m, s, v = map(float, input().split())
    n, m, s = int(n), int(m), int(s)
    edges = []
    for _ in range(m):
        a, b, r1, c1, r2, c2 = map(float, input().split())
        a, b = int(a), int(b)
        edges.append((a, b, r1, c1))
        edges.append((b, a, r2, c2))

    maxi = {i:0.0 for i in range(1, n + 1)}
    maxi[s] = v

    for t in range(n):
        updated = False
        for x, y, rate, cms in edges:
            if maxi[x] > cms:
                new = (maxi[x] - cms) * rate
                if new > maxi[y] + 1e-12:
                    maxi[y] = new
                    updated = True

            if y == s and maxi[s] > v:
                print("YES")
                return

        if t == n - 1 and updated:
            print('YES')
            return

        if not updated:
            break

    print('NO')


if __name__ == '__main__':
    main()