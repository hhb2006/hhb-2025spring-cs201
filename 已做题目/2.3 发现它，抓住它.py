class Cases:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, a, b):
        r1 = self.find(a)
        r2 = self.find(b)
        if r1 != r2:
            if self.rank[r1] < self.rank[r2]:
                self.parent[r1] = r2
            else:
                self.parent[r2] = r1
                if self.rank[r1] == self.rank[r2]:
                    self.rank[r1] += 1


def main():
    vis = set()
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        cases = Cases(2 * n + 1)
        for _ in range(m):
            s, x, y = input().split()
            x, y = int(x), int(y)
            r1, r2 = cases.find(x), cases.find(y)
            if s == 'A':
                if x not in vis or y not in vis:
                    print('Not sure yet.')
                elif r1 == r2:
                    print('In the same gang.')
                elif abs(r1 - r2) == n:
                    print('In different gangs.')
                else:
                    print('Not sure yet.')
            elif s == 'D':
                vis.add(x)
                vis.add(y)
                cases.union(x, y + n)
                cases.union(x + n, y)
        #print(cases.parent)


if __name__ == '__main__':
    main()