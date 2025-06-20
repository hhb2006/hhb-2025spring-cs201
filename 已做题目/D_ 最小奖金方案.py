n, m = map(int, input().split())
prize = {i: 100 for i in range(n)}
wins = {i: set() for i in range(n)}
loses = {i: set() for i in range(n)}
vis = set()
cost, l = 0, 0

for _ in range(m):
    winner, loser = map(int, input().split())
    wins[winner].add(loser)
    loses[loser].add(winner)

for _ in range(n):
    for team in range(n):
        if not wins[team] and not team in vis:
            l = team
            vis.add(l)
            break

    cost += prize[l]
    for w in loses[l]:
        prize[w] = max(prize[w], prize[l] + 1)
        wins[w].remove(l)

print(cost)