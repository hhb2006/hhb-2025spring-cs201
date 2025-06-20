from functools import lru_cache


@lru_cache(maxsize=None)
def avl_min_nodes(m):
    if m == 0:
        return 0
    elif m == 1:
        return 1
    else:
        return avl_min_nodes(m - 1) + avl_min_nodes(m - 2) + 1

n = int(input())
min_nodes = avl_min_nodes(n)
print(min_nodes)