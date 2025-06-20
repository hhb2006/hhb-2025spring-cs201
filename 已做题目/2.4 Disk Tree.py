class Doc:
    def __init__(self, name = ''):
        self.name = name
        self.kids = []

    def unfold(self, layer):
        if layer == -1:
            res = []
        else:
            res = [' ' * layer + self.name]

        if not self.kids:
            return res

        self.kids.sort(key = lambda x: x.name)

        for k in self.kids:
            res += k.unfold(layer + 1)
        return res


def main():
    n = int(input())
    root, names, vis, cnt = Doc(), set(), [], 0

    for _ in range(n):
        docs = list(map(Doc, input().split('\\')))
        lth = len(docs)
        for i in range(lth):
            if docs[i].name not in names:
                names.add(docs[i].name)
                vis.append(docs[i])
                cnt += 1
            else:
                for j in range(cnt):
                    if docs[i].name == vis[j].name:
                        docs[i] = vis[j]
            if i == 0:
                root.kids.append(docs[0])
            else:
                docs[i - 1].kids.append(docs[i])

    disk = root.unfold(-1)

    for i in range(len(disk)):
        print(disk[i])


if __name__ == '__main__':
    main()