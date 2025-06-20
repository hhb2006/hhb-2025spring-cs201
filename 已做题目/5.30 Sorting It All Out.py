from collections import deque, defaultdict

def kahn_check(adj, nodes):
    """
    改进的 Kahn 算法，用来判断当前图是否：
      - 有环，返回 0
      - 唯一拓扑序，返回该序列 list
      - 多解，返回 None
    """
    in_deg = {u: 0 for u in nodes}
    for u in adj:
        for v in adj[u]:
            in_deg[v] += 1

    q = deque(u for u in nodes if in_deg[u] == 0)
    topo = []
    unique = True
    while q:
        if len(q) > 1:
            unique = False
        u = q.popleft()
        topo.append(u)
        for v in adj[u]:
            in_deg[v] -= 1
            if in_deg[v] == 0:
                q.append(v)

    if len(topo) < len(nodes):
        return 0      # 有环
    return topo if unique else None

def forward_reachable(adj, start, pos, hi):
    """
    从 start 沿出边做 BFS，只收集那些 pos[w] ≤ hi 的节点。
    """
    seen = {start}
    q = deque([start])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if v not in seen and pos[v] <= hi:
                seen.add(v)
                q.append(v)
    return seen

def solve():
    import sys
    for line in sys.stdin:
        line = line.strip().split()
        if not line:
            continue
        n, m = map(int, line)
        if n == 0 and m == 0:
            break

        # 节点 A, B, ..., chr(ord('A')+n-1)
        nodes = [chr(ord('A') + i) for i in range(n)]
        adj   = defaultdict(list)

        # 初始序列就是 A, B, C, ...
        order = nodes[:]
        pos   = {u:i for i,u in enumerate(order)}

        def insert_edge(u, v):
            """
            插入 u->v：
            1) 如果 pos[u] < pos[v]，无需调整
            2) 否则
               F = 所有能从 v 出发（沿原图）到达且 pos[...] ≤ pos[u] 的节点
               若 u∈F 则成环，返回 False
               否则把 F 从 order 中摘出，插到 u 之后，更新 pos，返回 True
            """
            adj[u].append(v)
            if pos[u] < pos[v]:
                return True

            F = forward_reachable(adj, v, pos, pos[u])
            if u in F:
                return False

            # 从 order 中删掉 F
            new_order = [w for w in order if w not in F]
            # 找 u 在删完 F 后的新位置
            idx = new_order.index(u)
            # 保持 F 在旧 order 中的相对次序
            F_list = [w for w in order if w in F]

            # 重建 order：u 之后插入 F_list
            order.clear()
            order.extend(new_order[:idx+1])
            order.extend(F_list)
            order.extend(new_order[idx+1:])

            # 更新 pos
            for i,w in enumerate(order):
                pos[w] = i
            return True

        # 读入每条关系，在线处理
        rels = [sys.stdin.readline().strip() for _ in range(m)]
        done = False
        for i, rel in enumerate(rels, start=1):
            u, v = rel.split('<')
            ok = insert_edge(u, v)
            if not ok:
                print(f"Inconsistency found after {i} relations.")
                done = True
                break
            chk = kahn_check(adj, nodes)
            if isinstance(chk, list):
                print(f"Sorted sequence determined after {i} relations: {''.join(chk)}.")
                done = True
                break

        if not done:
            print("Sorted sequence cannot be determined.")

if __name__ == "__main__":
    solve()