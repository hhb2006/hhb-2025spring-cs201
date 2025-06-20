n = int(input())
dic = dict()
for i in range(n):
    lis = list(map(int, input().split()))
    t = lis[0]
    for j in range(1, t + 1):
        if lis[j] not in dic:
            dic[lis[j]] = [-1] * n
        dic[lis[j]][i] = 1

m = int(input())
items = [(a, b) for a, b in dic.items()]
items.sort(key = lambda x: x[0])
for _ in range(m):
    test = list(map(int, input().split()))
    check_indices = [i for i in range(n) if test[i] != 0]
    res = [od for od, txt in items
           if all(txt[i] == test[i] for i in check_indices)]
    if res:
        print(*res)
    else:
        print('NOT FOUND')


# http://cs101.openjudge.cn/practice/04093/
"""
BETTER VERSION:

import sys

def main():
    n = int(sys.stdin.readline())
    
    # 预处理：每个键的掩码，记录出现在哪些组（位置为1）
    key_masks = {}
    for i in range(n):
        parts = list(map(int, sys.stdin.readline().split()))
        t = parts[0]
        for key in parts[1:]:
            if key not in key_masks:
                key_masks[key] = 0
            key_masks[key] |= (1 << i)  # 标记该键在第i组出现过
    
    # 按键排序，避免每次查询排序
    sorted_keys = sorted(key_masks.keys())
    
    m = int(sys.stdin.readline())
    for _ in range(m):
        test = list(map(int, sys.stdin.readline().split()))
        # 生成需求掩码：test[i]=1的位置必须存在，test[i]=-1的位置必须不存在
        require_yes = 0  # 必须存在的位（test[i]=1）
        require_no = 0   # 必须不存在的位（test[i]=-1）
        for i in range(n):
            val = test[i]
            if val == 1:
                require_yes |= (1 << i)
            elif val == -1:
                require_no |= (1 << i)
        
        # 快速筛选符合条件的键
        res = []
        for key in sorted_keys:
            mask = key_masks[key]
            # 检查条件：必须存在的位全为1，且必须不存在的位全为0
            if (mask & require_yes) == require_yes and (mask & require_no) == 0:
                res.append(str(key))
        
        if res:
            print(' '.join(res))
        else:
            print('NOT FOUND')

if __name__ == "__main__":
    main()
"""