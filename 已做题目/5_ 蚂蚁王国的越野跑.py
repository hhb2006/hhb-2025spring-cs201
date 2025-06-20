def merge_sort(arr):
    if len(arr) <= 1:
        return 0, arr
    mid = len(arr) // 2
    cnt1, arr1 = merge_sort(arr[:mid])
    cnt2, arr2 = merge_sort(arr[mid:])
    cnt3, arr3 = merge(arr1, arr2)
    return cnt1 + cnt2 + cnt3, arr3

def merge(front, back):
    merged = []
    i, j, cnt = 0, 0, 0
    while i < len(front) and j < len(back):
        if front[i] < back[j]:
            merged.append(front[i])
            cnt += len(back) - j
            i += 1
        else:
            merged.append(back[j])
            j += 1
    merged.extend(front[i:])
    merged.extend(back[j:])
    return cnt, merged


n = int(input())
ants = [int(input()) for _ in range(n)]
res, lis = merge_sort(ants)
print(res)