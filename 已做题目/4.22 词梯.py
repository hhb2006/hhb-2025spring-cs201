from collections import deque


def is_connected(a, b):
    diff =sum(a[i] != b[i] for i in range(4))
    if diff == 1:
        return True
    return False


def build_graph(words):
    word_set = set(words)
    if 'a' <= words[0][0] <= 'z':
        mark = 'a'
    else:
        mark = 'A'
    dic, n = {w: [] for w in words}, len(words)
    if n ** 2 <= 25:
        for i in range(n):
            for j in range(n):
                if i != j and is_connected(words[i], words[j]):
                    dic[words[i]].append(words[j])
    else:
        for i in range(n):
            for j in range(4):
                for k in range(26):
                    new_word = words[i][:j] + chr(k + ord(mark)) + words[i][j + 1:]
                    if new_word in word_set and new_word != words[i]:
                        dic[words[i]].append(new_word)
    return dic


def main():
    n = int(input())
    graph = build_graph([input() for _ in range(n)])
    start, end = input().split()
    vis = set(start)
    q = deque([(start, [start])])
    while q:
        vertex, path = q.popleft()
        if vertex == end:
            print(*path)
            return
        for word in graph[vertex]:
            if word not in vis:
                q.append((word, path + [word]))
                vis.add(word)
    print('NO')


if __name__ == '__main__':
    main()