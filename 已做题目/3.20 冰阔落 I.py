import sys



def main():
    inp = sys.stdin.read().split()
    ptr = 0
    while ptr < len(inp):
        n = int(inp[ptr])
        m = int(inp[ptr + 1])
        ptr += 2
        parent = list(range(n + 1))

        def find(u):
            while parent[u] != u:
                parent[u] = parent[parent[u]]
                u = parent[u]
            return u

        for _ in range(m):
            x = int(inp[ptr])
            y = int(inp[ptr + 1])
            ptr += 2
            fx = find(x)
            fy = find(y)
            if fx == fy:
                print("Yes")
            else:
                parent[fy] = fx
                print("No")

        roots = set()
        for i in range(1, n + 1):
            roots.add(find(i))
        roots = sorted(roots)
        print(len(roots))
        print(' '.join(map(str, roots)))


if __name__ == "__main__":
    main()